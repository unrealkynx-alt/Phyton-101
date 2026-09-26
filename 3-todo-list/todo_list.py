import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

tasks = load_tasks()

while True:
    print("\n=== To-Do List ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option (1-4):  ")

    if choice == "1":
        if not tasks:
            print("Your to-do list is currently empty.")
        else:
            print("Your tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "2":
        new_task = input("Enter task description:  ")
        if new_task:
            tasks.append(new_task)
            save_tasks(tasks)
            print(f"Added: '{new_task}'")
        else:
            print("Task cannot be empty.")

    elif choice == "3":
        if not tasks:
            print("Your to-do list are currently empty.")
        else:
            print("\nTasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            task_num = input("Enter a task number to remove:  ")

            if task_num.isdigit():
                task_index = int(task_num) - 1

            if 0 <= task_index < len (tasks):
                removed_task = tasks.pop(task_index)
                save_tasks(tasks)
                print(f"Removed: '{removed_task}'")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Bye-bye!")
        break

    else:
        print("Invalid input, please pick a number between 1 and 4.")