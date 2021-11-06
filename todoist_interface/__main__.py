import json
import settings
from todoist import TodoistAPI
from gitlab import GitlabAPI
import utils

if __name__ == '__main__':

    # initialise the settings
    config = settings.read_config("todoist_interface.yml")

    # initialise Todoist and Gitlab
    todoist = TodoistAPI(config['todoist']['token'])
    gitlab = GitlabAPI(config["gitlab"]["url"], config["gitlab"]["token"])

    # Get the Todoist tasks
    tasks = todoist.get_get_tasks_by_filter("@gitlab")

    # Get the Gitlab issues
    # issues = gitlab.get_issues_by_assignee("zweili")

    # Create a list of issues that are not in Todoist
    issues = json.loads('[{"state":"opened","description":"Ratione dolores corrupti mollitia soluta quia.","author":{"state":"active","id":18,"web_url":"https://gitlab.example.com/eileen.lowe","name":"Alexandra Bashirian","avatar_url":null,"username":"eileen.lowe"},"milestone":{"project_id":1,"description":"Ducimus nam enim ex consequatur cumque ratione.","state":"closed","due_date":null,"iid":2,"created_at":"2016-01-04T15:31:39.996Z","title":"v4.0","id":17,"updated_at":"2016-01-04T15:31:39.996Z"},"project_id":1,"assignees":[{"state":"active","id":1,"name":"Administrator","web_url":"https://gitlab.example.com/root","avatar_url":null,"username":"root"}],"assignee":{"state":"active","id":1,"name":"Administrator","web_url":"https://gitlab.example.com/root","avatar_url":null,"username":"root"},"type":"ISSUE","updated_at":"2016-01-04T15:31:51.081Z","closed_at":null,"closed_by":null,"id":76,"title":"Consequatur","created_at":"2016-01-04T15:31:51.081Z","moved_to_id":null,"iid":6,"labels":["foo","bar"],"upvotes":4,"downvotes":0,"merge_requests_count":0,"user_notes_count":1,"due_date":"2016-07-22","web_url":"http://gitlab.example.com/my-group/my-project/issues/6","references":{"short":"#6","relative":"my-group/my-project#6","full":"my-group/my-project#6"},"time_stats":{"time_estimate":0,"total_time_spent":0,"human_time_estimate":null,"human_total_time_spent":null},"has_tasks":true,"task_status":"10 of 15 tasks completed","confidential":false,"discussion_locked":false,"issue_type":"issue","_links":{"self":"http://gitlab.example.com/api/v4/projects/1/issues/76","notes":"http://gitlab.example.com/api/v4/projects/1/issues/76/notes","award_emoji":"http://gitlab.example.com/api/v4/projects/1/issues/76/award_emoji","project":"http://gitlab.example.com/api/v4/projects/1"},"task_completion_status":{"count":0,"completed_count":0}}]')
    missing_tasks = utils.get_missing_tasks(tasks, issues)
    if missing_tasks:
        todoist.create_tasks(missing_tasks)
        exit(0)
    print("Nothing new to add.")
