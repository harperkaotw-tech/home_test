import json
import time
import requests
from common.logger import api_logger


def api_request(method, url, headers=None, params=None):
    start = time.time()
    api_logger.info(f"api url ==>> {url}")
    api_logger.info(f"api method==>> {method}")

    if headers:
        api_logger.info(f"api request headers ==>> {json.dumps(headers, indent=4, ensure_ascii=False)}")

    if params:
        api_logger.info(f"api request params ==>> {json.dumps(params, indent=4, ensure_ascii=False)}")

    response = requests.request(method=method, url=url, headers=headers, params=params)

    response_time = round(time.time() - start, 5)
    api_logger.info(f"api Response Time==>> {response_time}")

    try:
        resp_text = json.dumps(response.json(), ensure_ascii=False, indent=4)
    except Exception:
        resp_text = response.text

    api_logger.info(f"api response json ==>> {resp_text}")

    return response
