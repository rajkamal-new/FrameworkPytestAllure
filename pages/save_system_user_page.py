from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base.page import Page


class SaveSysUserPage(Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.__user_role = By.ID, "systemUser_userType"
        self.__employee_name = By.ID, "systemUser_employeeName_empName"
        self.__emp_results = By.CSS_SELECTOR, ".ac_results>ul>li"
        self.__username = By.ID, "systemUser_userName"
        self.__status = By.ID, "systemUser_status"
        self.__password = By.ID, "systemUser_password"
        self.__confirm_pwd = By.ID, "systemUser_confirmPassword"
        self.__save_btn = By.ID, "btnSave"
        self.__error_msgs_loc = By.CSS_SELECTOR, "span.validation-error[generated='true']"

    def click_save(self):
        self._click(self.__save_btn)
        return self

    def select_user_role(self, role):
        self._select(self.__user_role, role)
        return self

    def select_employee_name(self, name):
        self.input_employee_name(name)
        self._find_element_by_text(self.__emp_results, name).click()
        return self

    def input_employee_name(self, name):
        self._input_text(self.__employee_name, name)
        return self

    def input_username(self, username):
        self._input_text(self.__username, username)
        return self

    def select_status(self, status):
        self._select(self.__status, status)
        return self

    def input_password(self, password):
        self._input_text(self.__password, password)
        return self

    def input_confirm_pwd(self, password):
        self._input_text(self.__confirm_pwd, password)
        return self

    def error_msg_displayed(self):
        return [element.text for element in self._find_elements(self.__error_msgs_loc)]

