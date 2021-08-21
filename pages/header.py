from selenium.webdriver.common.by import By

from pages.base.page import Page


class Header(Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.__welcome_text = By.ID, "welcome"
        self.__logout_link = By.CSS_SELECTOR, "[href$='logout']"
        self.__first_level_menu = By.CSS_SELECTOR, ".firstLevelMenu"
        self.__second_level_menu = By.CSS_SELECTOR, ".firstLevelMenu+ul>li>a"
        self.__third_level_menu = By.CSS_SELECTOR, ".firstLevelMenu+ul>li>a+ul>li>a"

        self.__menu_loc_list = [self.__first_level_menu, self.__second_level_menu, self.__third_level_menu]

    def click_welcome(self):
        self._click(self.__welcome_text)
        return self

    def click_logout(self):
        self._click(self.__logout_link)
        return self


    def wait_for_login_page(self):
        return self._wait_for_page("login")


    def move_to_page_by_menu(self, menus):
        menu_list = menus.split(",")

        items = list(zip(self.__menu_loc_list,menu_list))

        for i in range(len(items)):
            element = self._find_element_by_text(items[i][0], items[i][1])
            if i != len(items)-1:
                self._move_to_element(element)
            else:
                self._move_to_element_and_click(element)

        return self