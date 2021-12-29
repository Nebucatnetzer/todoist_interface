import json
import requests

from todoist_interface import mantishub

import mocks


def test_mantishub_init():
    api = mantishub.MantishubAPI("mantistoken")
    assert api.token == "mantistoken"


def test_mantishub_get_tickets(monkeypatch, example_tickets):

    def mock_get(*args, **kwargs):
        return mocks.MockResponse(example_tickets)

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_get)
    api = mantishub.MantishubAPI("mantistoken")
    tickets = api.get_tickets()
    assert tickets[0]['content'] == "[Sample issue title](https://contria.mantishub.io/view.php?id=1)"


def test_covert_to_todoist(example_tickets):
    issues = json.loads(example_tickets)
    tasks = mantishub.convert_to_todoist(issues["issues"])
    assert tasks == [
        {'content': '[Sample issue title](https://contria.mantishub.io/view.php?id=1)',
         'label_ids': [2158784659]}
    ]
