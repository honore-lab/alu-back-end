#!/usr/bin/python3
"""Export all employees tasks to JSON"""

import json
import requests


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    data = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")

        data[user_id] = []

        for task in todos:
            if task.get("userId") == user.get("id"):
                data[user_id].append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })

    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)