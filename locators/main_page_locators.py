from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка "Войти в аккаунт"
    BUTTON_LOGIN = (By.XPATH, './/button[text() = "Войти в аккаунт"]')
    # Кнопка "Личный кабинет"
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]/parent::a')
    # Кнопка "Оформить заказ"
    BUTTON_MAKE_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')
    # Кнопка "Конструктор"
    BUTTON_CONSTRUCTOR = (By.XPATH, '//p[text() = "Конструктор"]')
    # Активный раздел конструктора
    SELECTED_SECTION = (By.XPATH, ('//div[contains(@class, "tab_tab_type_current")]'))
    # Надпись "Соберите бургер"
    CONSTRUCTOR_TITLE = (By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]/h1')
    # Заголовок "Булки" конструкторе
    BUNS_TITLE = (By.XPATH, '//span[text() = "Булки"]')
    # Заголовок "Соусы" конструкторе
    SAUCES_TITLE = (By.XPATH, '//span[text() = "Соусы"]')
    # Заголовок "Начинки" конструкторе
    FILLINGS_TITLE = (By.XPATH, '//span[text() = "Начинки"]')
    # Кнопка "Лента заказов"
    BUTTON_ORDERS = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li')
    # Флюоресцентная булка R2-D3
    R2_D3_BUN = (By.XPATH, '(.//p[contains(@class, "BurgerIngredient_ingredient__text")])[1]')
    # Заголовок окна "Детали ингредиента"
    INGREDIENT_DETAIL_TITLE = (By.XPATH, '//h2[contains(@class, "Modal_modal__title") and contains(text(), "Детали")]')
    # Кнопка закрыть окно "Детали ингредиента"
    BUTTON_CLOSE_INGREDIENT_DETAIL = (By.XPATH, '//section[contains(@class, '
                                    '"Modal_modal_opened")]//button[contains(@class, "close")]')
    # Картинка "Флюоресцентная булка R2-D3"
    R2_D3_BUN_PICTURE = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]')
    # Корзина для ингредиентов
    BASKET = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')
    # Наполнение корзины
    BASKET_CONTENT = (By.CSS_SELECTOR, '.constructor-element_pos_top .constructor-element__row')
    # Счетчик ингредиентов
    INGREDIENT_COUNTER = (By.XPATH, '//a[contains(@class, "BurgerIngredient_ingredient")]//'
                                    'p[contains(@class, "counter_counter__num")]')
    # Окно подтверждения заказа
    CONFIRM_ORDER_WINDOW = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/div[contains'
                                             '(@class, "Modal_modal__container")]')
    # Номер заказа в окне подтверждения
    NUMBER_CONFIRM_ORDER_WINDOW = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2')
    # Кнопка закрыть подтвержденние заказа
    BUTTON_CLOSE_CONFIRM_ORDER_WINDOW = (By.XPATH, '//button[contains(@class, "Modal_modal__close_modified")]')
