#!/usr/bin/python3
"""Displays an employee's TODO list progress using a REST API."""
import requests
import sys


if __name__ == "__main__":
    base = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]
    user = requests.get("{}/users/{}".format(base, user_id)).json()
    todos = requests.get("{}/todos".format(base),
                         params={"userId": user_id}).json()
    done = [t for t in todos if t.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    for task in done:
        print("\t {}".format(task.get("title")))