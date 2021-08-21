import logging
import time

import allure
import pytest
from allure_commons.types import AttachmentType
from hamcrest import *
import inspect

def verify(driver, result, expected):
    try:

        assert_that(result, is_(expected))
    except AssertionError as e:

        time_str = time.strftime("%Y%m%d-%H%M%S")
        allure.attach(driver.get_screenshot_as_png(), name=f"{inspect.stack()[1][3]}_{time_str}",
                  attachment_type=AttachmentType.PNG)
        pytest.fail()


def logging():
    pass


