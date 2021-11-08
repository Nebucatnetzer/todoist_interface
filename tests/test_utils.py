import todoist_interface.utils as utils


def test_get_missing_tasks():
    """
    Test if the issues_to_check are in the list of tasks
    """
    tasks = [{'id': '1', 'content': 'task 1'},
             {'id': '2', 'content': 'task 2'}]
    issues_to_check = [{'id': '1', 'content': 'task 1'},
                       {'id': '3', 'content': 'task 3'},
                       {'id': '2', 'content': 'task 2'}]
    missing_should_be = [{'id': '3', 'content': 'task 3'}]
    missing_tasks = utils.get_missing_tasks(tasks, issues_to_check)
    assert missing_tasks == missing_should_be


def test_get_missing_tasks_without_tasks():
    """
    Test if the issues_to_check are in the list of tasks
    """
    tasks = []
    issues_to_check = [{'id': '1', 'content': 'task 1'},
                       {'id': '3', 'content': 'task 3'},
                       {'id': '2', 'content': 'task 2'}]
    missing_tasks = utils.get_missing_tasks(tasks, issues_to_check)
    assert missing_tasks == issues_to_check
