"""Collects tasks from Gitlab and Mantishub and adds them to Todoist."""

import sys

import mantishub
import settings
import utils

from todoist import TodoistAPI
from gitlab import GitlabAPI


if __name__ == "__main__":
    # initialise the settings
    config = settings.read_config("todoist_interface.yml")

    # initialise Todoist and Gitlab
    todoist = TodoistAPI(config["todoist"]["token"])

    # Setup the todoist tasks
    tasks = []

    # Gitlab
    gitlab_labeled_tasks = []
    gitlab_tasks = []
    if "gitlab" in config:
        gitlab = GitlabAPI(
            config["gitlab"]["url"],
            config["gitlab"]["token"],
            config["gitlab"]["assignee"],
        )

        # Get the Gitlab tasks
        gitlab_tasks = gitlab.get_issues()
        # Get the Todoist tasks labeled gitlab
        gitlab_labeled_tasks = todoist.get_get_tasks_by_filter("@gitlab")
        if gitlab_labeled_tasks:
            tasks.extend(gitlab_labeled_tasks)

    # Mantishub
    mantis_labeled_tasks = []
    mantishub_tasks = []
    if "mantishub" in config:
        # Get the Mantishub tasks
        mantishub_tasks = mantishub.get_tickets(token=config["mantishub"]["token"])
        # Get the Todoist tasks labeled mantishub
        mantis_labeled_tasks = todoist.get_get_tasks_by_filter("@mantis")
        if mantis_labeled_tasks:
            tasks.extend(mantis_labeled_tasks)

    # Check if there are any tasks to add to Todoist
    missing_gitlab_tasks = []
    if gitlab_tasks:
        missing_gitlab_tasks.extend(utils.get_missing_tasks(tasks, gitlab_tasks))

    missing_mantis_tasks = []
    if mantishub_tasks:
        missing_mantis_tasks.extend(utils.get_missing_tasks(tasks, mantishub_tasks))

    if missing_gitlab_tasks or missing_mantis_tasks:
        if missing_gitlab_tasks:
            todoist.create_tasks(
                missing_gitlab_tasks,
                [
                    "gitlab",
                ],
            )
        if missing_mantis_tasks:
            todoist.create_tasks(
                missing_mantis_tasks,
                [
                    "mantis",
                ],
            )
        sys.exit(0)
    print("Nothing new to add.")
