import json

from todoist_interface.mantishub import MantishubAPI


def test_mantishub_init():
    mantishub = MantishubAPI("mantistoken")
    assert mantishub.token == "mantistoken"


def test_mantishub_get_tickets():
    mantishub = MantishubAPI("mantistoken")
    tickets = mantishub.get_tickets()
    assert len(tickets) > 0


def test_covert_to_todoist(example_tickets):
    mantis = MantishubAPI("token")
    issues = json.loads(example_tickets)

    tasks = mantis.convert_to_todoist(issues["issues"])
    assert tasks == [
        {'content': '[Sample issue title](https://contria.mantishub.io/view.php?id=1)',
         'label_ids': [2158784659]}
    ]
