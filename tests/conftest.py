import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from helpers import *
from data import Data
import requests

@pytest.fixture(params=['chrome'])
def driver(request):
    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
    elif request.param == 'chrome':
        options = Options()
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--incognito')
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
    driver.get(Data.BASE_PAGE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def create_and_delete_new_user():
    payload = {
        'email': random_email(),
        'password': random_pass(),
        'name': random_name()
    }
    response = requests.post(Data.USER_REGISTER_URL, data=payload)
    response_body = response.json()

    yield payload, response_body

    access_token = response_body['accessToken']
    requests.delete(Data.DELETE_USER_URL, headers={'Authorization': access_token})

@pytest.fixture
def create_user_and_order_and_delete(create_and_delete_new_user):
    access_token = create_and_delete_new_user[1]['accessToken']
    headers = {'Authorization': access_token}
    payload = {'ingredients': [
        '61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa6c',
        '61c0c5a71d1f82001bdaaa76', '61c0c5a71d1f82001bdaaa79'
    ]}
    response_body = requests.post(Data.CREATE_ORDER_URL, data=payload, headers=headers)

    yield access_token, response_body

    requests.delete(Data.DELETE_USER_URL, headers={'Authorization': access_token})

@pytest.fixture
def set_token(driver, create_and_delete_new_user):
    driver.get(Data.BASE_PAGE_URL)
    user_data = create_and_delete_new_user[1]
    access_token = user_data.get('accessToken')
    refresh_token = user_data.get('refreshToken')
    driver.execute_script(f'window.localStorage.setItem("accessToken", "{access_token}");')
    driver.execute_script(f'window.localStorage.setItem("refreshToken", "{refresh_token}");')