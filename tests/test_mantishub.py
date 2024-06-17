import json
import requests

import mocks

from todoist_interface import mantishub


def test_mantishub_get_tickets(monkeypatch, example_tickets):

    def mock_get(*_, **__):
        return mocks.MockResponse(example_tickets)

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_get)
    tickets = mantishub.get_tickets(token="1234")
    assert (
        tickets[0]["content"]
        == "[Sample issue title](https://contria.mantishub.io/view.php?id=1)"
    )


def test_covert_to_todoist(example_tickets):
    issues = json.loads(example_tickets)
    tasks = mantishub._convert_to_todoist(issues["issues"])
    assert tasks == [
        {
            "content": "[Sample issue title](https://contria.mantishub.io/view.php?id=1)",
            "label_ids": [2158784659],
        }
    ]
