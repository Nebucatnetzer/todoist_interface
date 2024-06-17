def get_missing_tasks(tasks: list, issues_to_check: list) -> list:
    """
    Check if tasks exists in tasks_to_check
    :param tasks: list of tasks
    :param issues_to_check: list of issues to check
    :return: A list of tasks not in Todoist
    """
    missing_tasks = []
    if tasks:
        for issue in issues_to_check:
            if issue["content"] not in [t["content"] for t in tasks]:
                missing_tasks.append(issue)
    else:
        return issues_to_check

    return missing_tasks
