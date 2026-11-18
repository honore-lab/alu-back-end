# alu-back-end

Python scripts that pull employee and TODO data from a REST API
([JSONPlaceholder](https://jsonplaceholder.typicode.com)) and export it
as text, CSV and JSON.

## Learning Objectives

- Why Bash scripting is not suited for this kind of task
- What an API and a REST API are
- What microservices are
- The CSV and JSON formats
- Pythonic naming styles (packages, modules, classes, variables,
  functions, constants) and CapWords / CamelCase

## Requirements

- Python 3 (tested with 3.4.3) on Ubuntu 14.04 LTS
- Only the standard library is used (`urllib`, `json`, `csv`, `sys`)
- Code follows PEP 8
- Every file starts with `#!/usr/bin/python3`, ends with a new line and
  is executable
- Imports are in alphabetical order
- Dictionary values are read with `.get()`
- Code does not run on import (`if __name__ == "__main__":`)
- Every module has a docstring

## Files (`api/`)

| File | Description |
|------|-------------|
| `0-gather_data_from_an_API.py` | Prints an employee's TODO list progress |
| `1-export_to_CSV.py` | Exports an employee's tasks to `USER_ID.csv` |
| `2-export_to_JSON.py` | Exports an employee's tasks to `USER_ID.json` |
| `3-dictionary_of_list_of_dictionaries.py` | Exports all employees' tasks to `todo_all_employees.json` |

## Usage

### 0. Gather data from an API

```
$ ./0-gather_data_from_an_API.py 2
Employee Ervin Howell is done with tasks(8/20):
	 distinctio vitae autem nihil ut molestias quo
	 voluptas quo tenetur perspiciatis explicabo natus
	 ...
```

### 1. Export to CSV

```
$ ./1-export_to_CSV.py 2
$ cat 2.csv
"2","Antonette","False","suscipit repellat esse quibusdam voluptatem incidunt"
"2","Antonette","True","distinctio vitae autem nihil ut molestias quo"
...
```

Format: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`

### 2. Export to JSON

```
$ ./2-export_to_JSON.py 2
$ cat 2.json
{"2": [{"task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": false, "username": "Antonette"}, ...]}
```

### 3. Dictionary of list of dictionaries

```
$ ./3-dictionary_of_list_of_dictionaries.py
$ cat todo_all_employees.json
{"1": [{"username": "Bret", "task": "delectus aut autem", "completed": false}, ...], "2": [...], ...}
```

## Notes

The scripts send a browser-style `User-Agent` header with each request,
because the API can reject the default Python one with an HTTP 403.

## Author

honore-lab

Project by Holberton School / ALU. Web Infrastructure, API.
