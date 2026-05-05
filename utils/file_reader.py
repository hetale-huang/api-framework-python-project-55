import json
from pathlib import Path

# 指向 tests/data 目录（稳定，不依赖运行路径）
BASE_PATH = Path(__file__).resolve().parents[1] / "tests" / "data"


def read_file(file_name: str) -> dict:
    # 防止传入 tests/data/xxx.json 导致重复拼路径
    file_name = Path(file_name).name

    file_path = BASE_PATH / file_name

    with open(file_path, mode="r", encoding="utf-8") as f:
        return json.load(f)