from todoist_interface.gitlab import GitlabAPI


def test_gitlab_init():
    gitlab = GitlabAPI("url", "token", "assignee")
    assert gitlab.url == "url" and gitlab.token == "token"
