import requests


class MantishubAPI:
    url = "https://contria.mantishub.io/api/rest/"

    def __init__(self, token: str):
        self.token = token

    def get_tickets(self):
        response = requests.get(
            self.url + "issues?filter_id=assigned",
            headers={"Authorization": self.token})
        tickets = response.json()
        return self.convert_to_todoist(tickets)

    def convert_to_todoist(self, tickets):
        for ticket in tickets:
            print(ticket)
        tasks = []
        return tasks
