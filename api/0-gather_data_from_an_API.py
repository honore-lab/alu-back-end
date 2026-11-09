#!/usr/bin/python3
"""Displays an employee's TODO list progress using a REST API."""
import json
import sys
import urllib.request


def get_json(url):
    """Returns the decoded JSON found at url."""
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = get_json(url + "users/" + user_id)
    todos = get_json(url + "todos?userId=" + user_id)
    done = [t.get("title") for t in todos if t.get("completed")]
    head = "Employee {} is done with tasks({}/{}):"
    print(head.format(user.get("name"), len(done), len(todos)))
    for title in done:
        print("\t {}".format(title))
        