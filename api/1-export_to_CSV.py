#!/usr/bin/python3
"""Export tasks to CSV"""

import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)

    user = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    username = user.get("username")

    filename = "{}.csv".format(user_id)

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])