class Todo:

    def __init__(self):
        self.my_task_list=[]

    def create_task(self):
        task = input("Enter the task: ")
        self.my_task_list.append(task)
        print(f"Task {task} added successfully.")

    def check_task(self):
        task=input("Enter the task to check: ")
        if task not in self.my_task_list:
            print("Task Not Present")
        else:
            print("Task is present")
        

    def delete_task(self):
        task=input("Enter the task to delete: ")
        if task in self.my_task_list:
            self.my_task_list.remove(task)
            print(f"Task {task} deleted")
        else:
            print("Task not found")

    def show_tasks(self):
        if not self.my_task_list:
            print("No tasks to show.")
        else:
            print("Your Tasks:")
            for idx, task in enumerate(self.my_task_list):
                print(f"{idx}. {task}")

    def menu(self):
        while True:
            print("TODO list")
            print("1. Create Task")
            print("2. Check Task")
            print("3. Delete Task")
            print("4. Show All Tasks")
            print("5. Exit")

            
            try:
                select_menu = int(input("Enter your choice (1 to 5): "))
                if select_menu == 1:
                    self.create_task()
                elif select_menu == 2:
                    self.check_task()
                elif select_menu == 3:
                    self.delete_task()
                elif select_menu == 4:
                    self.show_tasks()
                elif select_menu == 5:
                    print("Exiting Todo App. Goodbye!")
                    break
                else:
                    print("Invalid menu selection. Try again.")
            except ValueError:
                print("Please enter a valid number.")       

todo=Todo()
todo.menu()