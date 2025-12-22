import datetime
import time
import threading

task_lists = []
running = True


# ---------------- ALARM THREAD ----------------
def alarm_checker():
    while running:
        now = datetime.datetime.now()
        for t in task_lists:
            if now >= t["time"] and not t["notified"]:
                print("\n🔔 ALARM 🔔")
                print("Task:", t["task"])
                print("Time reached:", t["time"])
                t["notified"] = True
        time.sleep(1)


# Start alarm thread
alarm_thread = threading.Thread(target=alarm_checker, daemon=True)
alarm_thread.start()

while True:
    print("\nWelcome to the To-Do List App!")
    print("1. Add Task with Date & Time")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    user_choice = input("Please enter your choice: ")

    # ADD TASK
    if user_choice == "1":
        task = input("Enter your task: ")

        date_input = input("Enter date (YYYY-MM-DD): ")
        time_input = input("Enter time (HH:MM): ")

        task_time = datetime.datetime.strptime(
            date_input + " " + time_input, "%Y-%m-%d %H:%M"
        )

        task__details = ({
            "task": task,
            "time": task_time,
            "notified": False
        })
        task_lists.append(task__details)

        print("Task added successfully!")

    # VIEW TASKS
    elif user_choice == "2":
        if not task_lists:
            print("No tasks available.")
        else:
            for i, t in enumerate(task_lists):
                print(f"{i+1}. {t['task']} at {t['time']}")

    # REMOVE TASK
    elif user_choice == "3":
        for i, t in enumerate(task_lists):
            print(f"{i+1}. {t['task']}")

        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(task_lists):
            task_lists.pop(index)
            print("Task removed successfully!")
        else:
            print("Invalid task number.")

    # EXIT
    elif user_choice == "4":
        print("Bye")
        break

    else:
        print("Invalid choice.")

 