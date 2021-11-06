import pytest
from todoist_interface.todoist import TodoistAPI


def test_todoist_init():
    todoist = TodoistAPI("1234")
    assert todoist.token == "1234"
