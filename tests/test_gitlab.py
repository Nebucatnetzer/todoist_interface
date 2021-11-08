from todoist_interface.gitlab import GitlabAPI
import json


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
