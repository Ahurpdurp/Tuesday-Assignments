task_list = [] 

def title_screen():
    number_choice = input("Select from the following menu: \n 1: Add task \n \
2: Delete task \n 3: View all tasks \n Q: Quit the menu \n Your Selection: ")
    while number_choice not in ["1","2","3","Q"]:
        number_choice = input("Please choose either 1, 2, 3, or Q: ")
    if number_choice == "Q":
        print("See you next time!")
        return
    elif number_choice == "1": 
        add_task()
    elif number_choice == "2":
        delete_task()
    elif number_choice == "3":
        view_tasks() 
    additional_action = ""
    while additional_action.lower() not in ["y","n"]:
        additional_action = input("Did you want to do anything else? (Y/N) ")
    if additional_action.lower() == "y":
        title_screen() 
    else:
        print("See you next time!")
        return


def add_task():
    task_name = input("What task would you like to add? ")
    task_priority = ""
    while task_priority.lower() not in ["low", "medium", "high"]:
        task_priority = input("What priority is your task? (Low, Medium, or High) ")
    new_task = {"Task": task_name, "Priority": task_priority}
    task_list.append(new_task)
    print("The task has been added!")

def delete_task():
    if not task_list:
        print("No current items to view.")
        return
    for index in range(len(task_list)):
        print(str(index+1) + ": " + task_list[index]["Task"] + " - " + task_list[index]["Priority"])
    delete_index = 0
    while int(delete_index)-1 not in range(0, len(task_list)):
        delete_index = input("Please type the number of the task you want to delete. If none, then press Q ")
        if delete_index.lower() == "q":
            return
    del task_list[int(delete_index) - 1]


def view_tasks():
    if not task_list:
        print("No current items to view.")
        return
    for index in range(len(task_list)):
        print(str(index+1) + ": " + task_list[index]["Task"] + " - " + task_list[index]["Priority"])

  


title_screen() 