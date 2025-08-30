tasks = []

def show_menu():
    print("\nTask Manager")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Remove task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        if not tasks:
            print("\nNo tasks in the list.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                status = "✓" if task['done'] else "✗"
                print(f"{i}. {task['name']} [{status}]")

    elif choice == "2":
        task_name = input("\nEnter task name: ")
        tasks.append({'name': task_name, 'done': False})
        print("Task added!")

    elif choice == "3":
        if not tasks:
            print("\nNo tasks to mark.")
        else:
            task_num = int(input("Enter task number to mark as done: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]['done'] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if not tasks:
            print("\nNo tasks to remove.")
        else:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Removed task: {removed['name']}")
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("\nGoodbye! Your tasks are saved only for this session.")
        break

    else:
        print("Invalid choice. Please enter 1-5.")
