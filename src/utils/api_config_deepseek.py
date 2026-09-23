from typing import Dict

from ._env import env_key, load_dotenv

load_dotenv()

class APIConfig_Deepseek:
    """API配置类"""
    def __init__(self):
        # API配置
        self.api_key = env_key("ARK_API_KEY")
        self.api_base="https://ark.cn-beijing.volces.com/api/v3"
        self.model_version = "deepseek-v3-250324"
        # self.model_version = "deepseek-r1-250120"

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
    
class APIConfig_GLM3:
    """API配置类"""
    def __init__(self):
        # API配置
        self.api_key = env_key("ARK_API_KEY")
        self.api_base="https://ark.cn-beijing.volces.com/api/v3"
        self.model_version = "chatglm3-130b-fc-v1.0"
        # self.model_version = "deepseek-r1-250120"

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

class APIConfig_MOON:
    """API配置类"""
    def __init__(self):
        # API配置
        self.api_key = env_key("ARK_API_KEY")
        self.api_base="https://ark.cn-beijing.volces.com/api/v3"
        self.model_version = "moonshot-v1-8k"
        # self.model_version = "deepseek-r1-250120"

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

class APIConfig_MISTRAL7B:
    """API配置类"""
    def __init__(self):
        # API配置
        self.api_key = env_key("ARK_API_KEY")
        self.api_base="https://ark.cn-beijing.volces.com/api/v3"
        self.model_version = "mistral-7b-instruct-v0.2"
        # self.model_version = "deepseek-r1-250120"

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
class APIConfig_DQ7B:
    """API配置类"""
    def __init__(self):
        # API配置
        self.api_key = env_key("ARK_API_KEY")
        self.api_base="https://ark.cn-beijing.volces.com/api/v3"
        self.model_version = "deepseek-r1-distill-qwen-7b-250120"
        # self.model_version = "deepseek-r1-250120"

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
    
class APIConfig_DQ32B:
    """API配置类"""
    def __init__(self):
        # API配置
        self.api_key = env_key("ARK_API_KEY")
        self.api_base="https://ark.cn-beijing.volces.com/api/v3"
        self.model_version = "deepseek-r1-distill-qwen-32b-250120"

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
    
class APIConfig_DL70B:
    """API配置类"""
    def __init__(self):
        # API配置
        self.api_key = env_key("QIANFAN_API_KEY")
        self.api_base = "https://qianfan.baidubce.com/v2"
        self.model_version = "deepseek-r1-distill-llama-70b"

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