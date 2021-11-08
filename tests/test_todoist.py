from todoist_interface.todoist import TodoistAPI


def test_init():
    todoist = TodoistAPI("1234")
    assert todoist.token == "1234"
