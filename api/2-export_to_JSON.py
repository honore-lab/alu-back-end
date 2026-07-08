#!/usr/bin/python3
"""
Gathers data from a REST API for a given employee ID and exports
all their tasks to a JSON file.
"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user_url = "{}users/{}".format(url, user_id)
    user_res = requests.get(user_url)
    username = user_res.json().get("username")

    todos_url = "{}todos?userId={}".format(url, user_id)
    todos_res = requests.get(todos_url)
    todos_data = todos_res.json()

    tasks_list = []
    for task in todos_data:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    json_payload = {str(user_id): tasks_list}
    filename = "{}.json".format(user_id)

    with open(filename, mode='w') as json_file:
        json.dump(json_payload, json_file)
