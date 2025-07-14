print("\nWelcome to Dimpal's To-Do List")
tasks = []

while True:
    print("\n📝 TO-DO LIST MENU ")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == "1":
        if len(tasks) == 0:
            print("You have no tasks yet.")
        else:
            print("Your Tasks:")
            i = 0
            for task in tasks:
                i = i + 1
                print(str(i) + ". " + task)
                print("Total tasks: " + str(len(tasks)))

    elif choice == "2":
        task = input("Write your task: ")
        tasks.append("❌ " + task)
        print("Task added successfully!")
        print("Total tasks: " + str(len(tasks)))

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
            print("Total tasks: " + str(len(tasks)))
        else:
            i = 0
            for task in tasks:
                i = i + 1
                print(str(i) + ". " + task)

            number = input("Enter task number to delete: ")
            if number.isdigit():
                index = int(number) - 1
                if index >= 0 and index < len(tasks):
                    deleted_task = tasks.pop(index)
                    print("Deleted task: " + deleted_task)
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")