import yaml


def read_config(config_path):
    with open(file=config_path, encoding="utf-8", mode="r") as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
        return cfg
