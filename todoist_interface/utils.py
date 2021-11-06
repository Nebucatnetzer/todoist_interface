def get_missing_tasks(tasks, issues_to_check):
    """
    Check if tasks exists in tasks_to_check
    :param tasks: list of tasks
    :param issues_to_check: list of issues to check
    :return: A list of tasks not in Todoist
    """
    missing_tasks = []
    for issue in issues_to_check:
        if issue["title"] not in [t["content"] for t in tasks]:
            content = "[{title}]({url})".format(title=issue["title"],
                                                url=issue["web_url"])
            missing_tasks.append({"content": content})

    return missing_tasks
