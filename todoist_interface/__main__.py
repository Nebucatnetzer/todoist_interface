import settings
from todoist import TodoistAPI
from gitlab import GitlabAPI

if __name__ == '__main__':

    # initialise the settings
    config = settings.read_config("todoist_interface.yml")

    todoist = TodoistAPI(config['todoist']['token'])
    gitlab = GitlabAPI(config["gitlab"]["url"], config["gitlab"]["token"])
    tasks = todoist.get_get_tasks_by_filter("@gitlab")
    print(tasks)
