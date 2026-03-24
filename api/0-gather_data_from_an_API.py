#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    employee_name = user.get("name")

    total_tasks = len(todos)
    done_tasks = 0

    for task in todos:
        if task.get("completed"):
            done_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done_tasks, total_tasks))

    for task in todos:
        if task.get("completed"):
            print("\t {}".format(task.get("title")))