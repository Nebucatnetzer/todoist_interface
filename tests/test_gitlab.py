import json
import requests

from todoist_interface.gitlab import GitlabAPI
import mocks


def test_init():
    gitlab = GitlabAPI("url", "token", "assignee")
    assert (gitlab.url == "url"
            and gitlab.token == "token"
            and gitlab.assignee == "assignee")


def test_covert_to_todoist(example_issues):
    gitlab = GitlabAPI("url", "token", "assignee")
    issues = json.loads(example_issues)

    tasks = gitlab.convert_to_todoist(issues)
    assert tasks == [
        {'content': '[Consequatur vero maxime deserunt laboriosam est voluptas dolorem.](http://gitlab.example.com/my-group/my-project/issues/6)',
         'label_ids': [2158782094]}]


def test_gitlab_get_tickets(monkeypatch, example_issues):

    def mock_get(*args, **kwargs):
        return mocks.MockResponse(example_issues)

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_get)
    gitlab = GitlabAPI("url", "token", "assignee")
    issues = gitlab.get_issues()
    assert issues[0][
        'content'] == "[Consequatur vero maxime deserunt laboriosam est voluptas dolorem.](http://gitlab.example.com/my-group/my-project/issues/6)"
