"""A class to retrieve and create tasks in Todoist."""

import json
import uuid

import requests


class TodoistAPI:
    url = "https://api.todoist.com/rest/v2/"

    def __init__(self, token: str):
        self.token = token

    def get_get_tasks_by_filter(self, todoist_filter: str) -> list:
        """
        Returns all tasks from todoist
        """
        response = requests.get(
            self.url + "tasks",
            headers={"Authorization": "Bearer " + self.token},
            params={"filter": todoist_filter},
            timeout=5,
        )
        return response.json()

    def create_tasks(self, tasks: list, labels: list) -> None:
        """
        Adds tasks to todoist
        """
        for task in tasks:
            requests.post(
                self.url + "tasks",
                headers={
                    "Content-Type": "application/json",
                    "X-Request-Id": str(uuid.uuid4()),
                    "Authorization": "Bearer " + self.token,
                },
                data=json.dumps({"content": task["content"], "labels": labels}),
                timeout=5,
            )
