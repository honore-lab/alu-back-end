#!/usr/bin/python3
"""Export tasks to JSON"""

import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)

    user = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    username = user.get("username")

    data = {user_id: []}

    for task in todos:
        data[user_id].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    filename = "{}.json".format(user_id)

    with open(filename, "w") as f:
        json.dump(data, f)