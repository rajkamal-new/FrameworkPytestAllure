
import pytest
from hamcrest import *

from utils import read_csv_data


@pytest.mark.usefixture("load_dashboard")
class TestHeader:

    @pytest.fixture(autouse=True)
    def init_dp(self, load_dashboard):
        self.dp = load_dashboard

    @pytest.mark.new
    @pytest.mark.parametrize("menus,url" , read_csv_data("menu_nav_data.csv"))
    def test_1_goto_menu(self, menus, url):
        self.dp.move_to_page_by_menu(menus)
        assert_that(self.dp._wait_for_page(url), is_(True))

    def test_2_logout(self):
        assert_that(self.dp.click_welcome().click_logout().wait_for_login_page(), is_(True))