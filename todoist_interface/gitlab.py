"""Get issues from Gitlab API and convert them to Todoist tasks."""

import requests

from requests.exceptions import HTTPError


def convert_to_todoist(issues: list) -> list:
    tasks = []
    for issue in issues:
        title = issue["title"]
        url = issue["web_url"]
        content = f"[{title}]({url})"
        tasks.append(
            {
                "content": content,
                "label_ids": [
                    2158782094,
                ],
            }
        )
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
        url = (
            self.url
            + "issues?assignee_username="
            + assignee
            + "&state=opened&scope=all"
        )
        response = requests.get(url, headers={"PRIVATE-TOKEN": self.token}, timeout=5)
        content = response.json()
        if response.status_code != 200:
            if content["error"]:
                raise HTTPError(
                    "\nFailed to get issues from Gitlab:\n",
                    f"{content['error']}\n",
                    f"{content['error_description']}",
                )

        return content

    def get_issues(self) -> list:
        issues = self.get_issues_by_assignee(self.assignee)
        return convert_to_todoist(issues)
