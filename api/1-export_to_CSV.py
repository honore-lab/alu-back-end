#!/usr/bin/python3
"""
Gathers data from a REST API for a given employee ID and exports
all their tasks to a CSV file.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_id = sys.argv[1]
        url = "https://jsonplaceholder.typicode.com"

        # Fetch user profile info safely
        user_res = requests.get("{}/users/{}".format(url, user_id))
        username = user_res.json().get("username")

        # Fetch user todos data safely
        todos_res = requests.get("{}/todos?userId={}".format(url, user_id))
        todos_data = todos_res.json()

        if username and todos_data:
            filename = "{}.csv".format(user_id)
            with open(filename, mode='w', newline='') as csv_file:
                # csv.QUOTE_ALL satisfies strict string quoting requirements
                writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
                for task in todos_data:
                    writer.writerow([
                        user_id,
                        username,
                        task.get("completed"),
                        task.get("title")
                    ])
