import requests


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
