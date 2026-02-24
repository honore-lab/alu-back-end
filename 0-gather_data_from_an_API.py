#!/usr/bin/python3
"""
Gather data from an API
"""

import requests
import sys


def get_employee_data(employee_id):
    """Fetch employee and TODO data"""
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user = user_response.json()
    todos = todos_response.json()

    return user, todos


if __name__ == "__main__":
    employee_id = sys.argv[1]

    user, todos = get_employee_data(employee_id)

    employee_name = user.get("name")

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, len(done_tasks), total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))