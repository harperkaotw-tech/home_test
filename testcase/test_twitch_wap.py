from selenium.webdriver.support.ui import WebDriverWait
from common.common import *
from object.twitch_wap_step import *


@allure.feature("Feature: Selenium")
@allure.story("Story: Use Selenium to do search")
class Test_Twitch_Wap_Flow_By_Selenium:
    @allure.title("Search {keyword} related video bt selenium")
    @pytest.mark.parametrize("wait_time, keyword, amount",
                        get_data_key("home_test.yml", "test_twitch_wap_flow"))
    def test_twitch_wap_flow(self, twitch_driver, wait_time, keyword, amount):
        """
        1. Set up the WAP environment.
        2. Click the Search tab to navigate to the search page.
        3. Input the keywords and press Enter to submit.
        4. Click the Video tab to display the video results.
        5. Scroll down twice.
        6. Click the first visible video.
        7. Take a screenshot.
        8. Close the browser.
        """

        wait = WebDriverWait(twitch_driver, wait_time)
        click_search_tab(wait)
        search_keyword(wait, keyword)
        open_videos_tab(wait)
        scroll_down(twitch_driver, amount)
        click_first_video(wait)
        take_screenshot(twitch_driver, "twitch_streamer.png")

@allure.feature("Feature: WAP API")
@allure.story("Story: Use API to do conduits")
class Test_Conduits_By_API:
    @allure.title("Create, update, delete conduits")
    @pytest.mark.parametrize("shard_count, update_shard_count, scenario",
                        get_data_key("home_test.yml", "test_conduits"))
    def test_conduits(self, twitch_token, shard_count, update_shard_count, scenario):
        """
        1. Create new conduits
        2. Update share amount
        3. Get conduits amount
        4. Delete conduits
        5. Check conduits amount
        """
        check_create_conduits(twitch_token, shard_count, scenario)
        check_update_conduits(twitch_token, update_shard_count)
        if scenario == 'success':
            check_delete_conduits(twitch_token)
