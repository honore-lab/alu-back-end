#!/usr/bin/python3
"""
Export employee TODO list to CSV
"""

import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    filename = "{}.csv".format(employee_id)

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow([
                employee_id,
                user.get("username"),
                task.get("completed"),
                task.get("title")
            ])