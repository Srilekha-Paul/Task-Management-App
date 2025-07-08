def task():
    tasks = []
    print("-----WELCOME TO THE TASK MANAGEMENT APP-----")

    total_task = int(input("Enter how many task you want to add = "))
    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i} = ")
        task.append(task_name)

        print(f"Today's tasks are\n{tasks}")

        while True:
            opperation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop"))
            if opperation == 1:
                add = input("Enter task you want to add =")
                tasks.append(add)
                print(f"Task {add} has been succesfully added...")
            elif opperation ==2:
                updated_val = input("Enter the task name you want to update = ")
                if updated_val in tasks:
                    up = input("Enter new task =")
                    ind = tasks.index("updated_val")
                    tasks[ind] = up
                    print(f"Update task {up}")