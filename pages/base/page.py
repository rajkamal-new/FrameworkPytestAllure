from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Page:

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 15)

    def _find_element(self, locator):
        return self._wait.until(EC.visibility_of_element_located(locator))

    def _find_elements(self, locator):
        return self._wait.until(EC.visibility_of_any_elements_located(locator))

    def _find_element_by_text(self, locator, text):
        elements = self._find_elements(locator)
        for element in elements:
            if element.text == text:
                return element

    def _click(self, locator):
        element = self._find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def _input_text(self, locator, text):
        self._find_element(locator).send_keys(text)

    def _get_text(self, locator):
        return self._find_element(locator).text

    def _wait_for_page(self, url):
       return  self._wait.until(EC.url_contains(url))

    def _move_to_element(self, ele_or_loc):
        if isinstance(ele_or_loc, tuple):
            ActionChains(self.driver).move_to_element(self._find_element(ele_or_loc)).perform()
        else:
            ActionChains(self.driver).move_to_element(ele_or_loc).perform()


    def _move_to_element_and_click(self, ele_or_loc):
        if isinstance(ele_or_loc, tuple):
            ActionChains(self.driver).move_to_element(self._find_element(ele_or_loc)).click().perform()
        else:
            ActionChains(self.driver).move_to_element(ele_or_loc).click().perform()

    def _select(self,locator,text):
        drop_down = Select(self._find_element(locator))
        drop_down.select_by_visible_text(text)

    def _get_current_url(self):
        return self.driver.current_url