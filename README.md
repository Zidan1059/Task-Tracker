# CLI Task Tracker 📝

A lightweight command-line interface (CLI) application built in Python to manage daily tasks. It stores data locally in a JSON file, meaning it's fast, entirely private, and requires no external databases.

## Features
* Add new tasks with timestamps.
* List all tasks in a clean terminal table.
* Mark tasks as complete using their unique ID.
* Persistent local storage using JSON.

## Usage

Add a new task:
`python task_tracker.py add "Buy groceries"`

List all tasks:
`python task_tracker.py list`

Mark a task as done:
`python task_tracker.py done 1`
