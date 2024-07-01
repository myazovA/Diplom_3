from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка "Войти в аккаунт"
    button_login = By.XPATH, './/button[text() = "Войти в аккаунт"]'
    # Кнопка "Личный кабинет"
    button_personal_account = (By.XPATH, '//p[text()="Личный Кабинет"]/parent::a')
    # Кнопка "Оформить заказ"
    button_make_order = (By.XPATH, '//button[text()="Оформить заказ"]')
    # Кнопка "Конструктор"
    button_constructor = (By.XPATH, '//p[text() = "Конструктор"]')
    # Активный раздел конструктора
    selected_section = (By.XPATH, ('//div[@class = '
                                  '"tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]'))
    # Надпись "Соберите бургер"
    constructor_title = (By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]/h1')
    # Заголовок "Булки" конструкторе
    buns_title = (By.XPATH, '//span[text() = "Булки"]')
    # Заголовок "Соусы" конструкторе
    sauces_title = (By.XPATH, '//span[text() = "Соусы"]')
    # Заголовок "Начинки" конструкторе
    fillings_title = (By.XPATH, '//span[text() = "Начинки"]')
    # Кнопка "Лента заказов"
    button_orders = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li')
    # Флюоресцентная булка R2-D3
    R2_D3_bun = (By.XPATH, '(.//p[@class="BurgerIngredient_ingredient__text__yp3dH"])[1]')
    # Заголовок окна "Детали ингредиента"
    ingredient_detail_title = (By.XPATH, '//h2[contains(@class, "Modal_modal__title") and contains(text(), "Детали")]')
    # Кнопка закрыть окно "Детали ингредиента"
    button_close_ingredient_detail = (By.XPATH, '//section[contains(@class, '
                                    '"Modal_modal_opened")]//button[contains(@class, "close")]')
    # Картинка "Флюоресцентная булка R2-D3"
    R2_D3_bun_picture = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]')
    # Корзина для ингредиентов
    basket = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')
    # Наполнение корзины
    basket_content = (By.CSS_SELECTOR, '.constructor-element_pos_top .constructor-element__row')
    # Счетчик ингредиентов
    ingredient_counter = (By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]//p['
                                     '@class="counter_counter__num__3nue1"][1]')
    # Окно подтверждения заказа
    confirm_order_window = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/div[contains'
                                             '(@class, "Modal_modal__container")]')
    # Номер заказа в окне подтверждения
    number_confirm_order_window = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2')
    # Кнопка закрыть подтвержденние заказа
    button_close_confirm_order_window = (By.XPATH, '//button[contains(@class, "Modal_modal__close_modified")]')
