#!/usr/bin/python3
"""
Module docstring: A Python script that exports an employee's TODO list
progress into a CSV file format.
"""

import csv
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

    file_name = f"{emp_id}.csv"
    with open(file_name, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            completed = str(task.get("completed"))
            title = task.get("title")
            writer.writerow([emp_id, username, completed, title])
            