import yaml
import os
import time
import pytest
import allure
from selenium.webdriver.chrome.service import Service as ChromeService
from common.logger import api_logger
from common.config import MOBILE_DEVICE_NAME
import configparser
import os
import yaml

try:
    from selenium import webdriver
except ImportError:
    webdriver = None

def load_ini(path: str):
    config = configparser.ConfigParser()
    config.read(path, encoding="utf-8")
    return config

def load_yaml(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def get_data_key(yaml_file_name: str, key: str):
    try:
        base_path = os.path.dirname(os.path.dirname(__file__))
        yaml_path = os.path.join(base_path, "data", yaml_file_name)
        yaml_data = load_yaml(yaml_path)
        return yaml_data.get(key, [])
    except Exception as ex:
        return []

@allure.step('Get chrome driver')
def chrome_driver(platform: str = 'web', headless:bool = False, incognito:bool = True, mobile:bool = True):
    match platform:
        case 'web':
            api_logger.info('Setup chrome options (web)')
            chrome_options = webdriver.ChromeOptions()

            if mobile:
                api_logger.info(f'Enable Chrome mobile emulation (web) - {MOBILE_DEVICE_NAME}')
                mobile_emulation = {"deviceName": MOBILE_DEVICE_NAME}
                chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

            if incognito:
                chrome_options.add_argument('--incognito')
            if headless:
                chrome_options.add_argument('--headless')

            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--no-sandbox')

            browser = webdriver.Chrome(options=chrome_options)

            if not mobile:
                browser.maximize_window()

    return browser

def check_response_value(actual_value, expect_value, msg, logger='api'):
    """
    Assert that actual_value equals expect_value, or contains it if is_fuzzy is True.

    Args:
        actual_value (Any): The value returned by the system.
        expect_value (Any): The expected value to check.
        msg (str): Description of the field or business logic being validated.
        logger (str or Logger): 'api', 'web', or a logger object.

    Raises:
        TypeError: If types of actual and expected values do not match.
        AssertionError: If the comparison result does not meet expectation.
    """
    loggers = {'api': api_logger}
    if logger in loggers:
        loggers[logger].info(f"Expect {msg} {expect_value}, Actual is {actual_value}.")

    allure.attach(
        name=f"Expect {msg} {expect_value}, Actual is {actual_value}.",
        body=f"expect value: {expect_value}\n actual value: {actual_value}"
    )

