#!/usr/bin/python3
"""Gather data from an API"""

import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)

    user = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    name = user.get("name")

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    done_count = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        name, done_count, total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))