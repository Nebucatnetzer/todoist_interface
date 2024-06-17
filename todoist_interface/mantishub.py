"""Get issues from Mantishub API and convert them to Todoist tasks."""

import requests


def _convert_to_todoist(tickets: list) -> list:
    # TODO: add a function to convert mantis priority to todoist priority
    tasks = []
    for ticket in tickets:
        url = "https://contria.mantishub.io/view.php?id=" + str(ticket["id"])
        title = ticket["summary"]
        content = f"[{title}]({url})"
        tasks.append(
            {
                "content": content,
                "label_ids": [
                    2158784659,
                ],
            }
        )
    return tasks


def get_tickets(
    token: str, url: str = "https://contria.mantishub.io/api/rest/"
) -> list:
    response = requests.get(
        url + "issues?filter_id=assigned",
        headers={"Authorization": token},
        timeout=5,
    )
    tickets = response.json()
    return _convert_to_todoist(tickets["issues"])
