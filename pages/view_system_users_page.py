from selenium.webdriver.common.by import By

from pages.base.page import Page



class ViewSysUsersPage(Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.__add_btn = By.ID, "btnAdd"


    def click_add(self):
        self._click(self.__add_btn)
        return self