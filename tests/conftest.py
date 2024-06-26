import pytest


@pytest.fixture
def example_tasks():
    tasks_json = '[{"id":2995104339,"project_id":2203306141,"section_id":7025,"parent_id":2995104589,"content":"Buy Milk","description":"","comment_count":10,"assignee":2671142,"assigner":2671362,"order":1,"priority":1,"url":"https://todoist.com/showTask?id=2995104339"},{"id":2995104339,"project_id":2203306141,"section_id":7025,"parent_id":2995104589,"content":"Buy Milk","description":"","comment_count":10,"assignee":2671142,"assigner":2671362,"order":1,"priority":1,"url":"https://todoist.com/showTask?id=2995104339"}]'
    return tasks_json


@pytest.fixture
def example_issues():
    issues_json = '[{"state":"opened","description":"Ratione dolores corrupti mollitia soluta quia.","author":{"state":"active","id":18,"web_url":"https://gitlab.example.com/eileen.lowe","name":"Alexandra Bashirian","avatar_url":null,"username":"eileen.lowe"},"milestone":{"project_id":1,"description":"Ducimus nam enim ex consequatur cumque ratione.","state":"closed","due_date":null,"iid":2,"created_at":"2016-01-04T15:31:39.996Z","title":"v4.0","id":17,"updated_at":"2016-01-04T15:31:39.996Z"},"project_id":1,"assignees":[{"state":"active","id":1,"name":"Administrator","web_url":"https://gitlab.example.com/root","avatar_url":null,"username":"root"}],"assignee":{"state":"active","id":1,"name":"Administrator","web_url":"https://gitlab.example.com/root","avatar_url":null,"username":"root"},"type":"ISSUE","updated_at":"2016-01-04T15:31:51.081Z","closed_at":null,"closed_by":null,"id":76,"title":"Consequatur vero maxime deserunt laboriosam est voluptas dolorem.","created_at":"2016-01-04T15:31:51.081Z","moved_to_id":null,"iid":6,"labels":["foo","bar"],"upvotes":4,"downvotes":0,"merge_requests_count":0,"user_notes_count":1,"due_date":"2016-07-22","web_url":"http://gitlab.example.com/my-group/my-project/issues/6","references":{"short":"#6","relative":"my-group/my-project#6","full":"my-group/my-project#6"},"time_stats":{"time_estimate":0,"total_time_spent":0,"human_time_estimate":null,"human_total_time_spent":null},"has_tasks":true,"task_status":"10 of 15 tasks completed","confidential":false,"discussion_locked":false,"issue_type":"issue","_links":{"self":"http://gitlab.example.com/api/v4/projects/1/issues/76","notes":"http://gitlab.example.com/api/v4/projects/1/issues/76/notes","award_emoji":"http://gitlab.example.com/api/v4/projects/1/issues/76/award_emoji","project":"http://gitlab.example.com/api/v4/projects/1"},"task_completion_status":{"count":0,"completed_count":0}}]'
    return issues_json


@pytest.fixture
def example_tickets():
    tickets_json = '{"issues":[{"id":1,"summary":"Sample issue title","description":"Sample issue description","project":{"id":1,"name":"mantisbt"},"category":{"id":135,"name":"General"},"reporter":{"id":1,"name":"vboctor","real_name":"Victor Boctor","email":"vboctor@example.com"},"status":{"id":10,"name":"new","label":"new","color":"#fcbdbd"},"resolution":{"id":10,"name":"open","label":"open"},"view_state":{"id":10,"name":"public","label":"public"},"priority":{"id":30,"name":"normal","label":"normal"},"severity":{"id":50,"name":"minor","label":"minor"},"reproducibility":{"id":70,"name":"have not tried","label":"have not tried"},"sticky":false,"created_at":"2017-04-23T13:12:28-04:00","updated_at":"2017-04-23T13:12:28-04:00","custom_fields":[{"field":{"id":4,"name":"The City"},"value":"Seattle"}],"history":[{"created_at":"2017-04-23T13:12:28-04:00","user":{"id":36771,"name":"vboctor","real_name":"Victor Boctor","email":"vboctor@example.com"},"type":{"id":1,"name":"issue-new"},"message":"New Issue"}]}]}'
    return tickets_json
