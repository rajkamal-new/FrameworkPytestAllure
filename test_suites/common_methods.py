import logging
import time

import allure
import pytest
from allure_commons.types import AttachmentType
from hamcrest import *
import inspect

from utils import logg

log = logg()

def verify(driver, result, expected):
    log.debug(f"result:{result}, expected:{expected}")
    try:
        assert_that(result, is_(expected))
    except AssertionError:
        log.error(f"{inspect.stack()[1][3]} case failed")
        time_str = time.strftime("%Y%m%d-%H%M%S")
        allure.attach(driver.get_screenshot_as_png(), name=f"{inspect.stack()[1][3]}_{time_str}",
                  attachment_type=AttachmentType.PNG)
        pytest.fail()