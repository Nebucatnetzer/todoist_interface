import json
import requests
import uuid

if __name__ == '__main__':
    # tasks = requests.get(
    #     "https://api.todoist.com/rest/v1/labels",
    #     headers={
    #         "Authorization": "Bearer f1d6ff420068f4323077ff3ce500d39e09713a27"
    #     }).json()

    # print(tasks)
    requests.post("https://api.todoist.com/rest/v1/tasks",
                  headers={
                      "Content-Type": "application/json",
                      "X-Request-Id": str(uuid.uuid4()),
                      "Authorization": "Bearer f1d6ff420068f4323077ff3ce500d39e09713a27"
                  },
                  data=json.dumps({
                      "content": "foo",
                      "description": "bar",
                      "label_id": [2158782094, ]
                  }))
