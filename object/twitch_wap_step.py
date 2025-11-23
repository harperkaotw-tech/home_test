import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from common.logger import web_logger
from common.common import *
from api.twitch_wap import *

################## Selenium ##################
@allure.step("Click the Search tab to the search page")
def click_search_tab(wait):
    elem = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//div[contains(@class,'CoreText') and normalize-space(text())='瀏覽']/ancestor::a[1]"
    )))
    elem.click()
    time.sleep(2)

@allure.step("Click the search box and input the keyword - {text}")
def search_keyword(wait, text):
    search = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//input[@type='search']"
    )))
    search.click()
    search.clear()
    time.sleep(2)
    search.send_keys(text)
    time.sleep(2)
    search.send_keys(Keys.ENTER)
    time.sleep(2)

@allure.step("Switch to the video tab to display the video results")
def open_videos_tab(wait):
    tab = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(@href,'type=videos')]")
    ))
    tab.click()
    time.sleep(3)

@allure.step("Scroll down the page for {times} time")
def scroll_down(driver, times):
    height = driver.execute_script("return window.innerHeight;")
    for _ in range(times):
        driver.execute_script(f"window.scrollBy(0, {height});")
        time.sleep(1.2)
    time.sleep(5)

@allure.step("Get the first visible video element (>=60% visible or closest to top)")
def get_first_visible_video(driver):
    return driver.execute_script(
        """
        const links = Array.from(document.querySelectorAll("a[href^='/videos/']"));
        const vh = window.innerHeight;

        const items = links.map(el => {
        const r = el.getBoundingClientRect();
            const h = r.height || 1;
            const visible = Math.max(0, Math.min(r.bottom, vh) - Math.max(r.top, 0));
            return { el, ratio: visible / h, top: r.top };
        }).filter(i => i.ratio > 0);

        if (items.length === 0) return null;

        const sixty = items.filter(i => i.ratio >= 0.6).sort((a,b) => a.top - b.top);
        if (sixty.length) return sixty[0].el;

        items.sort((a,b) => a.top - b.top);
        return items[0].el;
        """)

@allure.step("Choose the first video")
def click_first_video(wait):
    video_link = wait.until(get_first_visible_video)
    video_href = video_link.get_attribute("href")
    web_logger.info(f"click the video: {video_href}")
    video_link.click()
    time.sleep(5)

@allure.step("take the screenshot")
def take_screenshot(driver, filename):
    driver.save_screenshot(filename)



################## API ##################
@allure.step("get conduits details")
def get_conduits_step(user_token, status_code=200):
    res = get_conduits(user_token)
    check_response_value(res.status_code, status_code, msg='response code')
    return res.json()

@allure.step("create new conduits with {shard_count}")
def create_conduits_step(user_token, shard_count, status_code=200):
    res = create_conduits(user_token, shard_count)
    check_response_value(res.status_code, status_code, msg='response code')
    return res.json()

@allure.step("updata share amount to {shard_count}")
def update_conduits_step(user_token, id, shard_count, status_code=200):
    res = update_conduits(user_token, id, shard_count)
    check_response_value(res.status_code, status_code, msg='response code')
    return res.json()

@allure.step("delete conduits")
def delete_conduits_step(user_token, id, status_code=204):
    res = delete_conduits(user_token, id)
    check_response_value(res.status_code, status_code, msg='response code')


################## Check function ##################
@allure.step("take the screenshot")
def check_create_conduits(user_token, shard_count, scenario):
    match scenario:
        case 'success':
            res = create_conduits_step(user_token, shard_count)
            check_response_value(res['data'][0]['shard_count'], shard_count, msg='shard count amount')

        case 'invalid_amount':
            res = create_conduits_step(user_token, shard_count, 400)
            check_response_value(res['error'], 'Bad Request', msg='response request')
            check_response_value(res['message'], 'shard_count must be less than or equal to 20000', msg='response request')

        case 'zero_amount':
            res = create_conduits_step(user_token, shard_count, 400)
            check_response_value(res['error'], 'Bad Request', msg='response request')
            check_response_value(res['message'], 'Missing required parameter \"shard_count\"', msg='response request')
           

@allure.step("take the screenshot")
def check_update_conduits(user_token, update_shard_count):
    res = get_conduits_step(user_token)
    res_id = res['data'][0]['id']
    res_update = update_conduits_step(user_token, res_id, update_shard_count)
    check_response_value(res_update['data'][0]['shard_count'], update_shard_count, msg='update shard count')


@allure.step("take the screenshot")
def check_delete_conduits(user_token):
    init_res = get_conduits_step(user_token)['data']
    ini_len = len(init_res)
    res_id = init_res[0]['id']
    res_delete = delete_conduits_step(user_token, res_id)
    last_res = get_conduits_step(user_token)['data']
    last_len = len(last_res)
    check_response_value(last_len, ini_len-1, msg='confuits amount')



