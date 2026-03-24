#!/usr/bin/python3
"""
Gather data from an API
"""
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)

    user = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    employee_name = user.get("name")

    total_tasks = len(todos)
    done_tasks = 0
    done_titles = []

    for task in todos:
        if task.get("completed") is True:
            done_tasks += 1
            done_titles.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done_tasks, total_tasks))

    for title in done_titles:
        print("\t {}".format(title))