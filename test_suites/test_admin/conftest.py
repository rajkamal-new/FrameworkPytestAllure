import pytest

from pages.login_page import LoginPage

@pytest.mark.usefixture("driver_manager")
@pytest.fixture(scope="class")
def load_dashboard(driver_manager):
    dp = LoginPage(driver_manager).login_as_admin()
    yield dp