"""各模型的 API 配置。

所有配置收敛在此：原先 7 个 ``api_config*.py`` 文件各自复制一份构造逻辑，
只差「密钥环境变量 / api_base / model_version」三个值。现在用一个基类
``_APIConfig`` 承载公共逻辑，子类只声明这三个常量。

密钥一律从环境变量读取（见 ``_env``），源码中不出现明文。
模型名对应论文中参与对比的各家服务：
ifopen（GPT-4o/GPT-4/o1）、aigcbest（Claude 3.7）、火山引擎方舟（DeepSeek/DouBao/
GLM3/Moonshot/Mistral/R1-Distill）、百度千帆（ERNIE/QwQ/DeepSeek-R1-Distill-Llama）。
"""
from typing import Dict

from ._env import env_key, load_dotenv

load_dotenv()

# 服务地址
IFOPEN_BASE = "https://beta.ifopen.ai/v1/"
AIGCBEST_BASE = "https://aigcbest.top/v1/"
ARK_BASE = "https://ark.cn-beijing.volces.com/api/v3"
QIANFAN_BASE = "https://qianfan.baidubce.com/v2"


class _APIConfig:
    """API 配置基类：子类只需覆盖 KEY_ENV / api_base / model_version。"""

    KEY_ENV = ""
    api_base = ""
    model_version = ""

    # 默认参数
    max_tokens = 2048
    temperature = 1.0
    timeout = 30.0
    max_image_size = (512, 512)
    image_quality = 85

    def __init__(self):
        self.api_key = env_key(self.KEY_ENV)

    def get_headers(self) -> Dict:
        """获取API请求头"""
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }


# ---- ifopen（GPT 系列） ----

class APIConfig(_APIConfig):
    KEY_ENV = "IFOPEN_API_KEY"
    api_base = IFOPEN_BASE
    model_version = "gpt-4o"


class APIConfig_GPT4(_APIConfig):
    KEY_ENV = "IFOPEN_API_KEY"
    api_base = IFOPEN_BASE
    model_version = "gpt-4"


class APIConfig_GPTO1(_APIConfig):
    KEY_ENV = "IFOPEN_API_KEY"
    api_base = IFOPEN_BASE
    model_version = "o1"


# ---- aigcbest（Claude） ----

class APIConfig1(_APIConfig):
    KEY_ENV = "AIGCBEST_API_KEY"
    api_base = AIGCBEST_BASE
    model_version = "claude-3-7-sonnet-20250219"


# ---- 火山引擎方舟 ----

class APIConfig_Deepseek(_APIConfig):
    KEY_ENV = "ARK_API_KEY"
    api_base = ARK_BASE
    model_version = "deepseek-v3-250324"


class APIConfig_DouBao(_APIConfig):
    KEY_ENV = "ARK_API_KEY"
    api_base = ARK_BASE
    model_version = "doubao-vision-pro-32k-241028"


class APIConfig_GLM3(_APIConfig):
    KEY_ENV = "ARK_API_KEY"
    api_base = ARK_BASE
    model_version = "chatglm3-130b-fc-v1.0"


class APIConfig_MOON(_APIConfig):
    KEY_ENV = "ARK_API_KEY"
    api_base = ARK_BASE
    model_version = "moonshot-v1-8k"


class APIConfig_MISTRAL7B(_APIConfig):
    KEY_ENV = "ARK_API_KEY"
    api_base = ARK_BASE
    model_version = "mistral-7b-instruct-v0.2"


class APIConfig_DQ7B(_APIConfig):
    KEY_ENV = "ARK_API_KEY"
    api_base = ARK_BASE
    model_version = "deepseek-r1-distill-qwen-7b-250120"


class APIConfig_DQ32B(_APIConfig):
    KEY_ENV = "ARK_API_KEY"
    api_base = ARK_BASE
    model_version = "deepseek-r1-distill-qwen-32b-250120"


# ---- 百度千帆 ----

class APIConfig_DL70B(_APIConfig):
    KEY_ENV = "QIANFAN_API_KEY"
    api_base = QIANFAN_BASE
    model_version = "deepseek-r1-distill-llama-70b"


class APIConfig_ERNIE(_APIConfig):
    KEY_ENV = "QIANFAN_API_KEY"
    api_base = QIANFAN_BASE
    model_version = "ernie-x1-32k-preview"


class APIConfig_QWQ32B(_APIConfig):
    KEY_ENV = "QIANFAN_API_KEY"
    api_base = QIANFAN_BASE
    model_version = "qwq-32b"
