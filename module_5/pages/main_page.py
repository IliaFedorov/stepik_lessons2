from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
#Data
login_assert_fail = "Login link is not presented"

class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        #return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), login_assert_fail