import settings
from todoist import TodoistAPI
from gitlab import GitlabAPI
from mantishub import MantishubAPI
import utils

if __name__ == '__main__':

    # initialise the settings
    config = settings.read_config("todoist_interface.yml")

    # initialise Todoist and Gitlab
    todoist = TodoistAPI(config['todoist']['token'])
    gitlab = GitlabAPI(config["gitlab"]["url"],
                       config["gitlab"]["token"],
                       config["gitlab"]["assignee"])
    mantishub = MantishubAPI(config["mantishub"]["token"])

    # Get the Todoist tasks
    tasks = []
    tasks.append(todoist.get_get_tasks_by_filter("@gitlab"))
    tasks.append(todoist.get_get_tasks_by_filter("@mantis"))

    # Get the Gitlab issues
    gitlab_tasks = gitlab.get_issues()
    mantishub_tasks = mantishub.get_tickets()
    missing_tasks = []
    missing_tasks.append(utils.get_missing_tasks(tasks, gitlab_tasks))
    missing_tasks.append(utils.get_missing_tasks(tasks, mantishub_tasks))

    if missing_tasks:
        todoist.create_tasks(missing_tasks)
        exit(0)
    print("Nothing new to add.")
