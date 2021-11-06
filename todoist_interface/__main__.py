import settings
from todoist import TodoistAPI
from gitlab import GitlabAPI
import utils

if __name__ == '__main__':

    # initialise the settings
    config = settings.read_config("todoist_interface.yml")

    # initialise Todoist and Gitlab
    todoist = TodoistAPI(config['todoist']['token'])
    gitlab = GitlabAPI(config["gitlab"]["url"], config["gitlab"]["token"])

    # Get the Todoist tasks
    tasks = todoist.get_get_tasks_by_filter("@gitlab")

    # Get the Gitlab issues
    issues = gitlab.get_issues_by_assignee("zweili")

    # Create a list of issues that are not in Todoist
    missing_tasks = utils.get_missing_tasks(tasks, issues)
    if missing_tasks:
        todoist.create_tasks(missing_tasks)
        exit(0)
    print("Nothing new to add.")
