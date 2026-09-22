import os
from typing import Dict

from ._env import env_key, load_dotenv

load_dotenv()

class APIConfig_DouBao:
    """API配置类"""
    def __init__(self):
        # API配置
        self.api_key = env_key("ARK_API_KEY")
        self.api_base="https://ark.cn-beijing.volces.com/api/v3"
        # self.model_version = "doubao-1-5-vision-pro-32k-250115"
        self.model_version = "doubao-vision-pro-32k-241028"

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