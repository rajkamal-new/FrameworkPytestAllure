import pytest

from hamcrest import *

from pages.login_page import LoginPage
from test_data.config.config import ADMIN
from test_suites.common_methods import verify
from utils import read_xl_data



@pytest.mark.usefixtures("driver_manager")
class TestLoginPage:

    @pytest.fixture(autouse=True)
    def load_login_page(self, driver_manager):
        self.lp = LoginPage(self.driver).load()
        print("Loaded Login Page")

    @pytest.fixture()
    def delete_cookie(self):
        yield
        self.driver.delete_all_cookies()
        print("Deleted cookies")

    @pytest.mark.negative_test
    def test_1_login_pass(self, delete_cookie):
        result = self.lp.login(ADMIN["username"], ADMIN["password"]).wait_for_dashboard_page()
        verify(self.driver, result, False)


    @pytest.mark.negative_test
    @pytest.mark.parametrize("username,password,msg", read_xl_data("login_data.xlsx","login_fail"))
    def test_2_login_fail(self, username, password, msg):
        result = self.lp.login(username, password).get_err_msg()
        verify(self.driver, result, msg)



