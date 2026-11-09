#!/usr/bin/python3
"""Exports an employee's TODO list to a CSV file named USER_ID.csv."""
import csv
import requests
import sys


if __name__ == "__main__":
    base = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]
    user = requests.get("{}/users/{}".format(base, user_id)).json()
    todos = requests.get("{}/todos".format(base),
                         params={"userId": user_id}).json()
    username = user.get("username")
    with open("{}.csv".format(user_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, username,
                             task.get("completed"), task.get("title")])
