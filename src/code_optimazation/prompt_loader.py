def load_prompt(file_path: str) -> str:
    """加载指定路径的 prompt 模板"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception:
        return ""
