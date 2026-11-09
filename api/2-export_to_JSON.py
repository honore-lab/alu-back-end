#!/usr/bin/python3
"""Exports an employee's TODO list to a JSON file named USER_ID.json."""
import json
import requests
import sys


if __name__ == "__main__":
    base = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]
    user = requests.get("{}/users/{}".format(base, user_id)).json()
    todos = requests.get("{}/todos".format(base),
                         params={"userId": user_id}).json()
    username = user.get("username")
    data = {user_id: [{"task": t.get("title"),
                       "completed": t.get("completed"),
                       "username": username} for t in todos]}
    with open("{}.json".format(user_id), "w") as json_file:
        json.dump(data, json_file)
