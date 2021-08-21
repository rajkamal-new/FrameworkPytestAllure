import time

import pytest
from hamcrest import *

from pages.save_system_user_page import SaveSysUserPage
from pages.view_system_users_page import ViewSysUsersPage
from utils import read_csv_data


@pytest.mark.usefixtures("load_dashboard")
class TestAddUser:

    @pytest.fixture(autouse=True)
    def load_save_system_user_page(self,load_dashboard):
        self.dp = load_dashboard
        self.dp.move_to_page_by_menu("Admin,User Management,Users")
        ViewSysUsersPage(self.driver).click_add()
        self.ssup = SaveSysUserPage(self.driver)

    @pytest.mark.add
    @pytest.mark.parametrize("role, emp_name, user_name, status, pwd, cnfm_pwd, exp_msg, scenario", read_csv_data("add_user.csv"))
    def test_add_user(self, role, emp_name, user_name, status, pwd, cnfm_pwd, exp_msg, scenario):
        self.ssup.select_user_role(role)

        if exp_msg == "Employee does not exist":
            self.ssup.input_employee_name(emp_name)
        else:
            self.ssup.select_employee_name(emp_name)

        self.ssup.input_username(user_name)\
            .select_status(status)\
            .input_password(pwd)\
            .input_confirm_pwd(cnfm_pwd)\

        self.ssup.click_save()

        if scenario == "pass":
            assert_that(self.ssup._wait_for_page(exp_msg),is_(True))
        else:
            assert_that(self.ssup.error_msg_displayed(), has_item(exp_msg))



"""
1.open browser
2.go to url
3.sign in
4. navigate to view sytem user page
5. click add
6.enter details in save system user page
7.click save
8.verify user added

"""