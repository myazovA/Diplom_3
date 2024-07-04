from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:

    # Карточка заказа
    ORDER_CARD = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]')
    # Заголовок карточки заказа
    ORDER_CARD_TITLE = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]//h2')
    # Номер заказа
    ORDER_NUM = (By.XPATH, '(//div[contains(@class, "OrderHistory_textBox")]'
                               '/p[contains(@class, "text_type_digits-default")])[1]')