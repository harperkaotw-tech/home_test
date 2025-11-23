from common.api import api_request
from common.config import TWITCH_API_URL
import allure


@allure.step("Get followed channel")
def get_conduits(user_token):
    url = TWITCH_API_URL + "/helix/eventsub/conduits"
    headers = {
        "Authorization": f"Bearer {user_token}",
        "Client-Id": 'wyw8mywhjevtgkhqzajrkucevjws7s'
    }
    params = {}

    return api_request("GET", url, headers=headers, params=params)

@allure.step("Get followed channel")
def create_conduits(user_token, shard_count):
    url = TWITCH_API_URL + "/helix/eventsub/conduits"
    headers = {
        "Authorization": f"Bearer {user_token}",
        "Client-Id": 'wyw8mywhjevtgkhqzajrkucevjws7s'
    }
    params = {
        'shard_count': shard_count
    }

    return api_request("POST", url, headers=headers, params=params)

@allure.step("Get followed channel")
def update_conduits(user_token, id, shard_count):
    url = TWITCH_API_URL + "/helix/eventsub/conduits"
    headers = {
        "Authorization": f"Bearer {user_token}",
        "Client-Id": 'wyw8mywhjevtgkhqzajrkucevjws7s'
    }
    params = {
        'id': id,
        'shard_count': shard_count
    }

    return api_request("PATCH", url, headers=headers, params=params)

@allure.step("Get followed channel")
def delete_conduits(user_token, id):
    url = TWITCH_API_URL + "/helix/eventsub/conduits"
    headers = {
        "Authorization": f"Bearer {user_token}",
        "Client-Id": 'wyw8mywhjevtgkhqzajrkucevjws7s'
    }
    params = {
        'id': id,
    }

    return api_request("DELETE", url, headers=headers, params=params)
