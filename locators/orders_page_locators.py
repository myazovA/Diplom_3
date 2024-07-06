from selenium.webdriver.common.by import By


class OrdersPageLocators:

    # Лента заказов
    ORDERS_SECTION = (By.XPATH, '//ul[contains(@class, "OrderFeed_list")]')
    # Заголовок ленты заказов
    ORDERS_TITLE = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1')
    # Карточка заказа в ленте
    ORDER_IN_FEED = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]')
    # Окно Детали заказа
    ORDER_DETAILS = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains'
                             '(@class, "Modal_orderBox")]')
    # Заголовок окна Детали заказа
    ORDER_DETAILS_TITLE = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, '
                                      '"Modal_orderBox")]//h2')
    # Счетчик заказов "Выполнено за все время"
    ALL_ORDERS_COUNTER = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    # Счетчик заказов "Выполнено за сегодня"
    DAILY_ORDERS_COUNTER = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
    # Заказ в разделе "В работе"
    ORDER_IN_PROGRESS = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li')
    # Номер заказа в разделе "В работе"
    ORDER_IN_PROGRESS_NUM = (By.XPATH, '//ul[contains(@class, '
                                             '"OrderFeed_orderListReady")]/li[contains(@class, '
                                             '"text_type_digits-default")]')
    # Номер заказа в ленте
    ORDER_NUM_IN_FEED = (By.XPATH, './/*[text()="{order_id}"]')