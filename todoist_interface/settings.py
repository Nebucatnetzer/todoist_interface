import yaml


def read_config():
    with open("todoist_interface.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
        return cfg
