#!/usr/bin/python3
"""
Export employee TODO list to JSON
"""

import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    username = user.get("username")

    tasks_list = []

    for task in todos:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {employee_id: tasks_list}

    filename = "{}.json".format(employee_id)

    with open(filename, "w") as json_file:
        json.dump(data, json_file)