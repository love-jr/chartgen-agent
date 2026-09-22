import os
from typing import Dict

from ._env import env_key, load_dotenv

load_dotenv()

class APIConfig_QWQ32B:
    """API配置类"""
    def __init__(self):
        # API配置

        # self.api_base = "https://aigcbest.top/v1/"
        # self.model_version = "claude-3-7-sonnet-20250219"
        self.api_key = env_key("QIANFAN_API_KEY")
        self.api_base = "https://qianfan.baidubce.com/v2"
        self.model_version = "qwq-32b"

        # 默认配置
        self.max_tokens = 2048
        self.temperature = 1.0
        self.timeout = 30.0
        self.max_image_size = (512, 512)
        self.image_quality = 85

    def get_headers(self) -> Dict:
        """获取API请求头"""
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }