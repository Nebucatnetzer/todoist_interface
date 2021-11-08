from todoist_interface.mantishub import MantishubAPI


def test_mantishub_init():
    mantishub = MantishubAPI("mantistoken")
    assert mantishub.token == "mantistoken"


def test_mantishub_get_tickets():
    mantishub = MantishubAPI("mantistoken")
    tickets = mantishub.get_tickets()
    assert len(tickets) > 0


def test_convert_to_todoist():
    assert False
