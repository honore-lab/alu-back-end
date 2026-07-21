#!/usr/bin/python3
"""
Module docstring: A Python script that exports an employee's TODO list
progress into a JSON file format.
"""

import json
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) < 2:
        exit(1)

    emp_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user details
    user_res = requests.get(f"{base_url}/users/{emp_id}")
    user_data = user_res.json()
    username = user_data.get("username")

    # Fetch tasks for the user
    todos_res = requests.get(f"{base_url}/todos?userId={emp_id}")
    todos = todos_res.json()

    task_list = []
    for task in todos:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username,
        }
        task_list.append(task_dict)

    out_data = {emp_id: task_list}
    file_name = f"{emp_id}.json"

    with open(file_name, mode="w", encoding="utf-8") as json_file:
        json.dump(out_data, json_file)
        