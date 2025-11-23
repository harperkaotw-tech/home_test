import requests
from common.common import *
from common.logger import web_logger
from common.config import TWITCH_BASE_URL


@allure.step("init twap order")
@pytest.fixture(scope="function")
def twitch_driver():
    driver = chrome_driver(platform="web", headless=False, mobile=True)
    web_logger.info("Launching Twitch mobile browser")
    driver.get(TWITCH_BASE_URL)
    web_logger.info(f"Opening Twitch: {TWITCH_BASE_URL}")
    time.sleep(2)

    yield driver

    driver.quit()
    web_logger.info("Closing browser")

@pytest.fixture(scope="session")
def twitch_token():
    cfg_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "account.ini")
    cfg = load_ini(cfg_path)["test_account"]

    payload = {
        "client_id": cfg["client_id"],
        "client_secret": cfg["client_secret"],
        "grant_type": "client_credentials",
    }

    res = requests.post("https://id.twitch.tv/oauth2/token", data=payload)
    check_response_value(res.status_code, 200, msg="status code")

    token = res.json().get("access_token")
    api_logger.info(f"[Twitch] OAuth token acquired: {token}")

    return token
