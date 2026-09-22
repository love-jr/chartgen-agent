import os
from typing import Dict

class APIConfig_DouBao:
    """火山引擎方舟 DouBao 视觉模型配置。

    密钥从环境变量 ARK_API_KEY 读取，不要写进源码。
    """
    def __init__(self):
        # API配置
        self.api_key = os.environ.get("ARK_API_KEY", "")
        self.api_base="https://ark.cn-beijing.volces.com/api/v3"
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
