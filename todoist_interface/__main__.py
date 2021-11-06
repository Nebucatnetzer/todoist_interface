import settings
from todoist import TodoistAPI

if __name__ == '__main__':

    # initialise the settings
    config = settings.read_config()

    todoist = TodoistAPI(config['todoist']['token'])
    tasks = todoist.get_get_tasks_by_filter("@gitlab")
    print(tasks)
