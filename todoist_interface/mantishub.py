import requests


def convert_to_todoist(tickets):
    # TODO: add a function to convert mantis priority to todoist priority
    tasks = []
    for ticket in tickets:
        url = ("https://contria.mantishub.io/view.php?id="
               + str(ticket["id"]))
        content = "[{title}]({url})".format(title=ticket["summary"],
                                            url=url)
        tasks.append({"content": content, "label_ids": [2158784659, ]})
    return tasks


class MantishubAPI:
    url = "https://contria.mantishub.io/api/rest/"

    def __init__(self, token: str):
        self.token = token

    def get_tickets(self):
        response = requests.get(
            self.url + "issues?filter_id=assigned",
            headers={"Authorization": self.token})
        tickets = response.json()
        return convert_to_todoist(tickets["issues"])
