#!/usr/bin/python3
"""
Gathers records from all employees via a REST API and exports
the unified structure to a JSON file.
"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    # Fetch all users and todos safely
    users_res = requests.get("{}/users".format(url))
    users_data = users_res.json()

    todos_res = requests.get("{}/todos".format(url))
    todos_data = todos_res.json()

    if users_data and todos_data:
        # Dictionary comprehension split across lines to respect PEP 8
        user_map = {
            u.get("id"): u.get("username") for u in users_data
        }

        all_employees_dict = {}

        # Initialize list container for every single user id
        for u_id in user_map.keys():
            all_employees_dict[str(u_id)] = []

        # Populate tasks directly matching respective user containers
        for task in todos_data:
            u_id = task.get("userId")
            if u_id in user_map:
                all_employees_dict[str(u_id)].append({
                    "username": user_map.get(u_id),
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })

        filename = "todo_all_employees.json"
        with open(filename, mode='w') as json_file:
            json.dump(all_employees_dict, json_file)
