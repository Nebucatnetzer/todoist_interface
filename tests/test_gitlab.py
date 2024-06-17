import json
import requests
import pytest

import mocks

from todoist_interface import gitlab


def test_init():
    api = gitlab.GitlabAPI("url", "token", "assignee")
    assert api.url == "url" and api.token == "token" and api.assignee == "assignee"


def test_covert_to_todoist(example_issues):
    issues = json.loads(example_issues)
    tasks = gitlab.convert_to_todoist(issues)
    assert tasks == [
        {
            "content": "[Consequatur vero maxime deserunt laboriosam est voluptas dolorem.](http://gitlab.example.com/my-group/my-project/issues/6)",
            "label_ids": [2158782094],
        }
    ]


@pytest.mark.skip(reason="Currently doesn't work because of the missing status_code")
def test_gitlab_get_tickets(monkeypatch, example_issues):

    def mock_get(*args, **kwargs):
        return mocks.MockResponse(example_issues)

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_get)
    api = gitlab.GitlabAPI("url", "token", "assignee")
    issues = api.get_issues()
    assert (
        issues[0]["content"]
        == "[Consequatur vero maxime deserunt laboriosam est voluptas dolorem.](http://gitlab.example.com/my-group/my-project/issues/6)"
    )
