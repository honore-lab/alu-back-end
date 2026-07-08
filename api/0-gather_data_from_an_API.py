#!/usr/bin/python3
"""
Gathers data from a REST API for a given employee ID and displays
their TODO list progress on standard output.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        user_id = sys.argv[1]
        url = "https://jsonplaceholder.typicode.com"

        # Fetch user info
        user_res = requests.get("{}/users/{}".format(url, user_id))
        user_data = user_res.json()
        employee_name = user_data.get("name")

        # Fetch all todos
        todos_res = requests.get("{}/todos".format(url))
        todos_data = todos_res.json()

        completed_tasks = []
        total_tasks = 0

        # Calculate matching sets
        for task in todos_data:
            if str(task.get("userId")) == str(user_id):
                total_tasks += 1
                if task.get("completed") is True:
                    completed_tasks.append(task.get("title"))

        done_count = len(completed_tasks)

        # First line print match
        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, done_count, total_tasks
        ))

        # Second and next lines: EXACTLY 1 tab and 1 space before title
        for title in completed_tasks:
            print("\t {}".format(title))
