#!/usr/bin/python3
"""
Exports all employees' TODO lists to a JSON file.
"""

import json
import requests


def fetch_data():
    """Fetch users and todos from API."""
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    return users, todos


def build_employee_tasks(users, todos):
    """Build dictionary of employees and their tasks."""
    all_employees = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        user_tasks = []
        for task in todos:
            if task.get("userId") == user_id:
                task_dict = {
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                }
                user_tasks.append(task_dict)

        all_employees[str(user_id)] = user_tasks

    return all_employees


def export_to_json(data):
    """Export data to JSON file."""
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    users_data, todos_data = fetch_data()
    result = build_employee_tasks(users_data, todos_data)
    export_to_json(result)