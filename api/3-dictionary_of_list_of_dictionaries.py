#!/usr/bin/python3
"""Export all employees' TODO lists to a single JSON file."""
import json
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
    users = fetch("{}/users".format(BASE_URL))
    todos = fetch("{}/todos".format(BASE_URL))
    data = {}
    for user in users:
        uid = user.get("id")
        data[str(uid)] = [
            {"username": user.get("username"),
             "task": t.get("title"),
             "completed": t.get("completed")}
            for t in todos if t.get("userId") == uid]
    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
