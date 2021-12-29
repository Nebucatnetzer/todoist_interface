import requests


def convert_to_todoist(issues):
    tasks = []
    for issue in issues:
        content = "[{title}]({url})".format(title=issue["title"],
                                            url=issue["web_url"])
        tasks.append({"content": content, "label_ids": [2158782094, ]})
    return tasks


class GitlabAPI:
    def __init__(self, url: str, token: str, assignee: str) -> None:
        self.url = url
        self.token = token
        self.assignee = assignee

    def get_issues_by_assignee(self, assignee: str) -> list:
        """
        Get all issues assigned to a specific user
        :param assignee: The username of the assignee
        :return: A list of issues assigned to the user
        """

        # Get all issues assigned to the user
        url = (self.url
               + 'issues?assignee_username='
               + assignee
               + '&state=opened&scope=all')
        response = requests.get(url, headers={'PRIVATE-TOKEN': self.token}, verify=False)
        issues = response.json()

        return issues

    def get_issues(self) -> list:
        issues = self.get_issues_by_assignee(self.assignee)
        return convert_to_todoist(issues)
