from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    CARD_ITEM_NAME = (By.XPATH, "//div/h1")
    CARD_ITEM_COST = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_ITEM_NAME = (By.CSS_SELECTOR, "#messages .alert")
    MESSAGE_ITEM_COST = (By.CSS_SELECTOR, "#messages .alert-info")

