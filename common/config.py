from pathlib import Path
import os

# 專案根目錄（config.py 在 common/ 裡，所以往上一層）
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# logs 根目錄
LOG_ROOT = PROJECT_ROOT / "logs"

# 各類 log 資料夾
API_LOG_PATH = LOG_ROOT / "api"
PERFORMANCE_LOG_PATH = LOG_ROOT / "performance"
WEBUI_LOG_PATH = LOG_ROOT / "webui"

# 這次作業要測的網站（可以寫死在這裡）
TWITCH_BASE_URL = "https://www.twitch.tv/"

TWITCH_API_URL = "https://api.twitch.tv"

# Mobile emulator 使用的裝置名稱
MOBILE_DEVICE_NAME = "iPhone SE"