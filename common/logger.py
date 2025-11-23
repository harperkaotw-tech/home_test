import logging
import time
import os
from common.config import (API_LOG_PATH, PERFORMANCE_LOG_PATH, WEBUI_LOG_PATH,)


class Logger:

    def __init__(self, logger_name, log_path, file_level=logging.INFO, console_level=logging.INFO):
        self.logname = os.path.join(str(log_path), f"{logger_name}_{time.strftime('%Y%m%d%H%M')}.log",)
        self.logger = logging.getLogger(logger_name)

        if not self.logger.hasHandlers():
            self.logger.setLevel(logging.INFO)
            formatter = logging.Formatter(
                "[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s]: %(message)s"
            )

            file_handler = logging.FileHandler(self.logname, mode="a", encoding="UTF-8")
            file_handler.setLevel(file_level)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

            console_handler = logging.StreamHandler()
            console_handler.setLevel(console_level)
            console_handler.setFormatter(formatter)

            if logger_name in ("ApiLog", "WebUILog"):
                self.logger.addHandler(console_handler)


api_logger = Logger(logger_name="ApiLog", log_path=API_LOG_PATH,).logger
performance_logger = Logger(logger_name="ApiPerformanceLog", log_path=PERFORMANCE_LOG_PATH,).logger
web_logger = Logger(logger_name="WebUILog",log_path=WEBUI_LOG_PATH,).logger
