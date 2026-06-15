tasks = []

def show_menu():
    print("\n=== To-Do List ===")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Exit")

while True:
    show_menu()

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
            continue

        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

        try:
            index = int(input("Enter task number to delete: "))
            removed = tasks.pop(index - 1)
            print(f"Deleted: {removed}")
        except (ValueError, IndexError):
            print("Invalid task number.")

    elif choice == "3":
        if not tasks:
            print("No tasks found.")
        else:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")