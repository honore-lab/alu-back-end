#!/usr/bin/python3
"""
Module docstring: A Python script that gathers employee TODO list progress
from a REST API and prints it to the standard output.
"""

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
    employee_name = user_data.get("name")

    # Fetch tasks for the user
    todos_res = requests.get(f"{base_url}/todos?userId={emp_id}")
    todos = todos_res.json()

    total_tasks = len(todos)
    done_tasks = [t for t in todos if t.get("completed") is True]
    number_of_done = len(done_tasks)

    print(
        f"Employee {employee_name} is done with tasks"
        f"({number_of_done}/{total_tasks}):"
    )

    for task in done_tasks:
        print(f"\t {task.get('title')}")
        