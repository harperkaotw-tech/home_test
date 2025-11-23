# home_test

1. Overview

This project is a small test playground that combines:

Twitch Helix API tests (e.g. /helix/eventsub/conduits)

Simple WAP (web) flows using Selenium

A custom logger that prints clear API logs

Pytest + Allure for test execution & reporting

2. Project Structure
home_test/
├── common/              # shared utilities 共用工具：logger、request wrapper、config loader...
│   ├── logger.py        # custom logging wrapper 自訂 logger
│   ├── api.py           # api_request() 封裝 requests
│   └── common.py        # 共用檢查函式，例如 check_response_value
├── object/              # step functions: Twitch API & WAP steps
│   └── twitch_wap_step.py
├── testcase/            # pytest test cases 測試案例
│   └── test_twitch_wap.py
├── config/
│   └── account.ini      # Twitch client_id / client_secret 設定檔
├── logs/                # 執行測試時產生的 log（會自動建立）
├── requirements.txt
└── README.md

3. Environment Setup
3.1 Python version
- Python 3.11

3.2 Install dependencies
pip install -r requirements.txt

4. Config Setup
config/account.ini
[test_account]
client_id = your_twitch_client_id
client_secret = your_twitch_client_secret

5. Test Cases
UI / WAP Flow (if enabled)
    Launch the Twitch page using Selenium
    Enter a keyword into the search bar and submit
    Call scroll_down(driver, times) to scroll the page multiple times
    Call get_first_visible_video(driver)
    Locate the first video link that is at least 60% visible within the viewport, and click it

API Flow
    Create, update, delete, and retrieve Conduits
    Perform validation and follow-up checks on each API action

6. Run Test
Selenium
    pytest -vs testcase/test_twitch_wap.py -k test_twitch_wap_flow

API
    pytest -vs testcase/test_twitch_wap.py -k test_conduits

GIF
