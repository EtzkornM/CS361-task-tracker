import os

# file where tasks are saved
TASK_FILE = "tasks.txt"
tasks = []

def print_header(title):
    width = 40

    print("\n" + "=" * width)
    print("|" + " " * (width - 2) + "|")
    print("|" + title.center(width - 2) + "|")
    print("|" + " " * (width - 2) + "|")
    print("=" * width)

# load tasks from file
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []

    with open(TASK_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

# save tasks to file
def save_tasks():
    with open(TASK_FILE, "w") as f:
        for t in tasks:
            f.write(t + "\n")

# show main menu
def menu():
    print_header("TASK MANAGER")

    print("Organize your tasks quickly and stay productive with simple commands.\n")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

# add task
def add_task():
    print_header("ADD TASK")
    print("Enter a task (or type 0 to return to main menu)\n")
    print("Double check your task before saving\n")

    task = input("Enter Task Description: ").strip()

    if task == "0":
        print("Returning to main menu...")
        return

    if task == "":
        print("empty task not allowed")
        return

    tasks.append(task)
    save_tasks()
    print("Your task has been saved!!")

    while True:
        print("\n1. Add another task")
        print("0. Return to main menu")

        choice = input("Enter Choice (0 or 1): ").strip()

        if choice == "1":
            return add_task()
        elif choice == "0":
            return
        else:
            print("invalid option")

# view tasks
def view_tasks():
    while True:
        print_header("VIEW TASKS")

        print("Choose what to view:")
        print("1. Active Tasks")
        print("2. Completed Tasks")
        print("3. All Tasks")
        print("0. Return to Main Menu")

        choice = input("Enter choice (0-3): ").strip()

        if choice == "0":
            print("Returning to main menu...")
            return

        # active tasks
        if choice == "1":
            print_header("ACTIVE TASKS")

            found = False
            for i, task in enumerate(tasks, 1):
                if not task.startswith("[x]"):
                    print(f"{i}. {task}")
                    found = True

            if not found:
                print("No active tasks.")

        # completed tasks
        elif choice == "2":
            print_header("COMPLETED TASKS")

            found = False
            for i, task in enumerate(tasks, 1):
                if task.startswith("[x]"):
                    print(f"{i}. {task[4:]}")
                    found = True

            if not found:
                print("No completed tasks.")

        # all tasks
        elif choice == "3":
            print_header("ALL TASKS")

            if len(tasks) == 0:
                print("No tasks found.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        else:
            print("Invalid option.")
            continue

        
        print("\n1. Back to View Menu")
        print("0. Return to Main Menu")

        back = input("Enter choice (0 or 1): ").strip()

        if back == "0":
            return
        elif back == "1":
            continue
        else:
            print("Invalid input, returning to view menu...")

# delete task
def delete_task():

    while True:

        if len(tasks) == 0:
            print("No tasks to delete.")
            input("Press Enter to return to main menu...")
            return

        print_header("DELETE TASK")
        print("WARNING: This action cannot be undone\n")

        # show tasks
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

        choice = input("\nEnter task number or name (0 to return): ").strip()

        if choice == "0":
            print("Returning to main menu...")
            return

        target_task = None

        # delete by number
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(tasks):
                target_task = tasks[index]
            else:
                print("Invalid task number.")
                continue

        # delete by name
        else:
            if choice in tasks:
                target_task = choice
            else:
                print("Task not found.")
                continue

        # confirmation step
        print(f"\nAre you sure you want to delete: '{target_task}'?")
        confirm = input("Confirm deletion (y/n): ").strip().lower()

        if confirm == "y":
            tasks.remove(target_task)
            save_tasks()
            print("Task deleted successfully.")

            # post-action menu 
            while True:
                print("\n1. Delete another task")
                print("0. Return to main menu")

                next_action = input("Enter choice: (0 or 1) ").strip()

                if next_action == "1":
                    break  # stays in delete loop
                elif next_action == "0":
                    return
                else:
                    print("Invalid option.")

        else:
            print("Deletion cancelled.")
            continue

# main loop
def main():
    global tasks
    tasks = load_tasks()

    while True:
        menu()
        choice = input("(Enter Choice 1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("bye")
            break
        else:
            print("invalid")

# run it
main()