from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:

    # Карточка заказа
    order_card = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]')
    # Заголовок карточки заказа
    order_card_title = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]//h2')
    # Номер заказа
    order_num = (By.XPATH, '(//div[contains(@class, "OrderHistory_textBox")]'
                               '/p[contains(@class, "text_type_digits-default")])[1]')