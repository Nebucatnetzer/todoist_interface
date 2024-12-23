from typing import Any

import yaml


def read_config(config_path: str) -> Any:
    with open(file=config_path, encoding="utf-8", mode="r") as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
        return cfg
