import argparse
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from the JSON file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    """Saves the current list of tasks to the JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    """Creates a new task and appends it to the list."""
    tasks = load_tasks()
    # Find the highest existing ID, default to 0 if the list is empty
    new_id = max([t["id"] for t in tasks], default=0) + 1
    
    task = {
        "id": new_id,
        "description": description,
        "done": False,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task: '{description}' (ID: {new_id})")

def list_tasks():
    """Displays all tasks in a formatted table."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found. Add one to get started!")
        return
    
    print("\nID  | Status | Date             | Description")
    print("-" * 55)
    for t in tasks:
        status = "[x]" if t["done"] else "[ ]"
        print(f"{t['id']:<3} | {status}  | {t['date']} | {t['description']}")
    print("-" * 55)

def complete_task(task_id):
    """Marks a specific task ID as done."""
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save_tasks(tasks)
            print(f"Task {task_id} marked as complete.")
            return
    print(f"Error: Task ID {task_id} not found.")

def main():
    parser = argparse.ArgumentParser(description="A simple CLI Task Tracker")
    subparsers = parser.add_subparsers(dest="command")

    # The 'add' command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="What do you need to do?")

    # The 'list' command
    subparsers.add_parser("list", help="List all current tasks")

    # The 'done' command
    complete_parser = subparsers.add_parser("done", help="Mark a task as complete")
    complete_parser.add_argument("id", type=int, help="The ID of the task to complete")

    args = parser.parse_args()

    # Route the command to the correct function
    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        complete_task(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()