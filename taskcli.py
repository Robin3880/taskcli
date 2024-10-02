import sys
import json
import os

def main():
    # Load current stored tasks into a variable
    with open("tasks.json", "r") as file:
        json_tasks = json.load(file)

    # Function to update the JSON file
    def update_json():
        with open("tasks.json", "w") as file:
            json.dump(json_tasks, file, indent=4)  # Added indentation for readability

    if len(sys.argv) < 2:
        print("No command provided.")
        return

    try:
        command = sys.argv[1]
        task = sys.argv[2].replace("\"", "") if len(sys.argv) > 2 else None

        if command == "add":                      # Add task command
            json_tasks[task] = "to-do"
            update_json()

        elif command == "delete":                 # Delete task command
            if task in json_tasks:
                del json_tasks[task]
                update_json()
            else:
                print(f"Task '{task}' not found.")

        elif command == "mark-in-progress":       # Mark-in-progress command
            if task in json_tasks:
                json_tasks[task] = "in-progress"
                update_json()
            else:
                print(f"Task '{task}' not found.")

        elif command == "mark-done":              # Mark-done command
            if task in json_tasks:
                json_tasks[task] = "done"
                update_json()
            else:
                print(f"Task '{task}' not found.")

        elif command == "list" and len(sys.argv) == 2:  # List all tasks
            for task, status in json_tasks.items():
                print(f"{task}: {status}")

        elif command == "list" and sys.argv[2] == "done":  # List done tasks
            for task, status in json_tasks.items():
                if status == "done":
                    print(f"{task}: {status}")

        elif command == "list" and sys.argv[2] == "to-do":  # List to-do tasks
            for task, status in json_tasks.items():
                if status == "to-do":
                    print(f"{task}: {status}")

        elif command == "list" and sys.argv[2] == "in-progress":  # List in-progress tasks
            for task, status in json_tasks.items():
                if status == "in-progress":
                    print(f"{task}: {status}")

        else:
            print(f"Unknown command: {command}")  # Handle incorrect commands

    except IndexError:
        print("Invalid arguments given.")

if __name__ == '__main__':
    main()