# home_test

1. Overview
'''
This project is a small test playground that combines:

Twitch Helix API tests (e.g. /helix/eventsub/conduits)

Simple WAP (web) flows using Selenium

A custom logger that prints clear API logs

Pytest + Allure for test execution & reporting
'''

2. Environment Setup
'''
2.1 Python version
- Python 3.11

2.2 Install dependencies
pip install -r requirements.txt
'''

3. Config Setup
'''
config/account.ini
[test_account]
client_id = your_twitch_client_id
client_secret = your_twitch_client_secret
'''

5. Test Cases
'''
UI / WAP Flow (if enabled)
    Launch the Twitch page using Selenium
    Enter a keyword into the search bar and submit
    Call scroll_down(driver, times) to scroll the page multiple times
    Call get_first_visible_video(driver)
    Locate the first video link that is at least 60% visible within the viewport, and click it

API Flow
    Create, update, delete, and retrieve Conduits
    Perform validation and follow-up checks on each API action
'''

5. Run Test
'''
Selenium
    pytest -vs testcase/test_twitch_wap.py -k test_twitch_wap_flow

API
    pytest -vs testcase/test_twitch_wap.py -k test_conduits
'''

## Demo

![Twitch Demo](./assets/twitch_demo.gif)


