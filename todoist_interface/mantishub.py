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
        # TODO: add a function to convert mantis priority to todoist priority
        # TODO: add a function to create the url
        tasks = []
        for ticket in tickets:
            url = "https:mantishub.com"
            content = "[{title}]({url})".format(title=ticket["summary"],
                                                url=url)
            tasks.append({"content": content, "label_ids": [2158784659, ]})
        return tasks
