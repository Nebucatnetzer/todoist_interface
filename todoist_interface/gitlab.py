import requests


class GitlabAPI:
    def __init__(self, url: str, token: str) -> None:
        self.url = url
        self.token = token

    def get_issues_by_assignee(self, assignee: str) -> list:
        """
        Get all issues assigned to a specific user
        :param assignee: The username of the assignee
        :return: A list of issues assigned to the user
        """

        # Get all issues assigned to the user
        url = (self.url
               + '/api/v4/issues?assignee_username='
               + assignee
               + '&state=opened')
        response = requests.get(url, headers={'PRIVATE-TOKEN': self.token})
        issues = response.json()

        return issues
