import pytest

from selenium.webdriver import Chrome, Firefox, Edge
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    """
    can pass --browser=browser_name as command line argument
    @browser_name: chrome, firefox, edge
    """
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope="session")
def driver_manager(request, pytestconfig):

    global driver
    browser = pytestconfig.getoption("browser")

    if browser == "chrome":
        driver = Chrome(executable_path=ChromeDriverManager().install())
    elif browser == "firefox":
        driver = Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "edge":
        driver = Edge(executable_path=EdgeChromiumDriverManager().install())

    driver.maximize_window()

    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)

    yield driver

    driver.close()
    if driver is not None:
        driver.quit()


# fixture scope
# a fixture is a function that will run before or after a test function
# scope - when it should run
# scope can be "session", "package", "module", "class", "function"
# by default the scope will be function
# autouse=True

# a fixture can use another fixture