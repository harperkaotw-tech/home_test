# home_test


1. Overview

This project is a small test playground that combines:

Twitch Helix API tests (e.g., /helix/eventsub/conduits)

Simple WAP (mobile web) UI flows using Selenium

A custom logger that prints clear API logs

Pytest + Allure for test execution and reporting

2. Environment Setup
2.1 Python Version
Python 3.11

2.2 Install Dependencies
pip install -r requirements.txt

3. Configuration
Edit the config file:
config/account.ini

[test_account]
client_id = your_twitch_client_id
client_secret = your_twitch_client_secret

4. Test Cases
4.1 UI / WAP Flow (if Selenium is enabled)

Steps performed in the UI flow:

Launch the Twitch WAP page using Selenium

Enter a keyword into the search bar and submit

Call scroll_down(driver, times) to scroll the page

Call get_first_visible_video(driver)

Locate the first video link that is at least 60% visible within the viewport

Click the video

4.2 API Flow

The API flow tests:

Create a Conduit

Update the Conduit

Delete the Conduit

Retrieve all Conduits

Validate response codes and response fields for each API action

5. Run Tests
Run UI (Selenium) test
pytest -vs testcase/test_twitch_wap.py -k test_twitch_wap_flow

Run Conduits API test
pytest -vs testcase/test_twitch_wap.py -k test_conduits

6. Generate Allure Report
allure serve ./report


## Demo

![Twitch Demo](image/twitch_demo.gif)


