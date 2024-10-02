import sys
import json
import os


def main():
    with open("tasks.json", "r") as file:           #loads current stored tasks into variable
        json_tasks = json.load(file)

    def update_json():                              #function to update the json file
        with open("tasks.json", "w") as file:
            json.dump(json_tasks, file)    

    if len(sys.argv) < 2:
        print("No command provided.")
        return
    try:
        if sys.argv[1] == "add":                      #add task command
            task = sys.argv[2].replace("\"", "")
            json_tasks[f"{task}"] = "to-do"
            update_json()
        elif sys.argv[1] == "delete":                 #delete task command
            del json_tasks[sys.argv[2].replace("\"","")]
            update_json()
        elif sys.argv[1] == "mark-in-progress":       #mark-in-progress command
            json_tasks[sys.argv[2].replace("\"","")] = "in-progress"
            update_json()  
        elif sys.argv[1] == "mark-done":              #mark-done command
            json_tasks[sys.argv[2].replace("\"","")] = "done"
            update_json()
        elif sys.argv[1] == "list" and len(sys.argv) == 2:  #list command
            for task in json_tasks:
                print(f"{task}: {json_tasks[task]}")
        elif sys.argv[1] == "list" and sys.argv[2] == "done": #list done command
            for task in json_tasks:
                if json_tasks[task] == "done":
                    print(f"{task}: {json_tasks[task]}")
        elif sys.argv[1] == "list" and sys.argv[2] == "to-do":  #list to-do command
            for task in json_tasks:
                if json_tasks[task] == "to-do":
                    print(f"{task}: {json_tasks[task]}")
        elif sys.argv[1] == "list" and sys.argv[2] == "in-progress":  #list in-progress command
            for task in json_tasks:
                if json_tasks[task] == "in-progress":
                    print(f"{task}: {json_tasks[task]}")
        else:
            print(f"Unknown command: {sys.argv[1]}")  # Handle  incorrect commands
    except IndexError:
        print("Invalid arguments given")

if __name__ == '__main__':
    main()