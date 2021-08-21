from selenium.webdriver.common.by import By

from pages.base.page import Page
from pages.header import Header
from test_data.config.config import ADMIN


class LoginPage(Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.__username_tbox = By.ID, "txtUsername"
        self.__password_tbox = By.ID, "txtPassword"
        self.__login_btn = By.ID, "btnLogin"
        self.__forgot_pass_link = By.CSS_SELECTOR, "[href$='ResetCode']"
        self.__err_msg_text = By.ID, "spanMessage"

    def load(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        return self

    def input_username(self, username):
        self._input_text(self.__username_tbox, username)
        return self

    def input_password(self, password):
        self._input_text(self.__password_tbox, password)
        return self

    def click_login(self):
        self._click(self.__login_btn)
        return self

    def get_err_msg(self):
        return self._get_text(self.__err_msg_text)

    def goto_forget_pass(self):
        self._click(self.__forgot_pass_link)
        # TODO - add ForgetPasswordPage

    def wait_for_dashboard_page(self):
        return self._wait_for_page("dashboard")

    def login(self, username, password):
        return self.input_username(username).input_password(password).click_login()

    def login_as_admin(self):
        self.load().login(ADMIN["username"], ADMIN["password"])\
            .wait_for_dashboard_page()
        return Header(self.driver)