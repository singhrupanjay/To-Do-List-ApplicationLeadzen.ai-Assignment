#Empty list where all the task is going to be stored
tasks = []

#Function to add task to list
def add_task():
    task = input("Enter New Task:")
    tasks.append(task)
    print("Task Added Successfully :")
    
#Function to print all the task added to the list 
def view_task():
    if len(tasks)== 0:
        print("No task to display.")
    else:
        for i,task in enumerate(tasks):
            print(f'{i+1}.{task}')

#Function to delete a task from the list
def delete_task():
    if len(tasks) == 0:
        print("No task to delete.")
    else:
        print("Tasks:")
        for i,task in enumerate(tasks):
            print(f'{i+1}.{task}')
        choice = int(input('Enter the task number to delete:'))

        if 0 < choice <= len(tasks):
            del tasks[choice-1]
            print("Task Deleted")
        else:
            print("Invalid task number.")
            
#Function to mark the completed task as Done
def completed_task():
    for i,task in enumerate(tasks):
            print(f'{i+1}.{task}')
    var1 = int(input("\nEnter number of task to mark as Done :"))
    s2 = (tasks[var1-1]) + " DONE"
    tasks[var1-1] = s2
    print(f'\nTask number {var1} marked Done Successfully!')
    view_task()

# main function    
def main():

    while True:
        print('\n\t===== To Do List =====')
        print("\t 1. Add task")
        print("\t 2. view task")
        print("\t 3. Delete task")
        print("\t 4. Mark Task complete")
        print("\t 5. Quit")

        choice = int(input("\tEnter your choice:"))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            completed_task()
        elif choice == 5:
            print("Exiting Application")
            break
        else:
            print('Invalid choice. Please try ')

if __name__== "__main__":
    main()
