from selenium.webdriver.common.by import By


class OrdersPageLocators:

    # Лента заказов
    orders_section = (By.XPATH, '//ul[contains(@class, "OrderFeed_list")]')
    # Заголовок ленты заказов
    orders_title = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1')
    # Карточка заказа в ленте
    order_in_feed = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]')
    # Окно Детали заказа
    order_details = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains'
                             '(@class, "Modal_orderBox")]')
    # Заголовок окна Детали заказа
    order_details_title = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, '
                                      '"Modal_orderBox")]//h2')
    # Счетчик заказов "Выполнено за все время"
    all_orders_counter = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    # Счетчик заказов "Выполнено за сегодня"
    daily_orders_counter = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
    # Заказ в разделе "В работе"
    order_in_progress = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li')
    # Номер заказа в разделе "В работе"
    order_in_progress_num = (By.XPATH, '//ul[contains(@class, '
                                             '"OrderFeed_orderListReady")]/li[contains(@class, '
                                             '"text_type_digits-default")]')
    # Номер заказа в ленте
    order_num_in_feed = (By.XPATH, './/*[text()="{order_id}"]')