#!/usr/bin/python3
"""Export an employee's TODO list to a JSON file."""
import json
import sys
import urllib.request

BASE_URL = "https://jsonplaceholder.typicode.com"
HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)",
           "Accept": "application/json"}


def fetch(url):
    """Fetch a URL and return the decoded JSON."""
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    user_id = int(sys.argv[1])
    user = fetch("{}/users/{}".format(BASE_URL, user_id))
    todos = fetch("{}/todos?userId={}".format(BASE_URL, user_id))
    data = {str(user_id): [
        {"task": t.get("title"),
         "completed": t.get("completed"),
         "username": user.get("username")} for t in todos]}
    with open("{}.json".format(user_id), "w") as f:
        json.dump(data, f)