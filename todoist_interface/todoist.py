import requests
import json


class TodoistAPI:
    url = "https://api.todoist.com/rest/v1/"

    def __init__(self, token: str):
        self.token = token

    def get_get_tasks_by_filter(self, filter: str):
        """
        Returns all tasks from todoist
        """
        response = requests.get(
            self.url + '/tasks',
            headers={'Authorization': 'Bearer ' + self.token},
            params={"filter": filter})
        return response.json()

    def add_tasks(self, tasks: list):
        """
        Adds tasks to todoist
        """
        for task in tasks:
            requests.post(self.url + '/tasks',
                          headers={'Authorization': 'Bearer ' + self.token},
                          data=json.dumps({
                              "content": task["content"],
                          }))
