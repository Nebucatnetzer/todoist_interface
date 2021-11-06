from todoist_interface import settings


def test_settings():
    config = settings.read_config("todoist_interface.yml.example")
    assert (config["gitlab"]["token"] == "gitlabtoken"
            and config["gitlab"]["url"] == "https://gitlab.example.com/api/v4/"
            and config["todoist"]["token"] == "todoisttoken"
            and config["gitlab"]["assignee"] == "muster"
            and config["mantishub"]["token"] == "mantistoken")
