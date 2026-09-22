"""从环境变量读取密钥的公共助手。

密钥不应写进源码。请通过环境变量或 .env 提供，例如：

    ARK_API_KEY=你的火山引擎方舟密钥
    QIANFAN_API_KEY=你的百度千帆密钥
    IFOPEN_API_KEY=你的 ifopen 密钥
    AIGCBEST_API_KEY=你的 aigcbest 密钥
"""
import os


def env_key(name, default=""):
    """读取环境变量中的密钥；缺失时返回 default（通常为空串）。"""
    return os.environ.get(name, default)


def load_dotenv(path=None):
    """可选：从项目根目录的 .env 读取 KEY=VALUE，不引入额外依赖。"""
    if path is None:
        path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
            ".env")
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as env_file:
        for line in env_file:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))
