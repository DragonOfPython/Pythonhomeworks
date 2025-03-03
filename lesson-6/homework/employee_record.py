# Employee ID, Name, Position, Salary

# Splitting tasks with function in python

def employee_record_list():
    print("\nProgram tasks:")
    print("1. Add new employee record")
    print("2. View all employee records")
    print("3. Search for an employee by Employee ID")
    print("4. Update an employee's information")
    print("5. Delete an employee record")
    print("6. Exit")

# 1. Add new employee record
def add_new_employee(employee_file):
    with open(employee_file, "a") as f:
        employee_ID = input("What is an employee's ID: ")
        employee_name = input("What is an employee's name: ")
        employee_position = input("What is an employee's position: ")
        employee_salary = input("How much is an employee's salary: ")
        f.write(f"{employee_ID}, {employee_name}, {employee_position}, {employee_salary}\n")
        print("New employee's records added")

# Display all employee records from "employees.txt".
def view_employees_record(employee_file):
    try:
        with open(employee_file, "r") as f:
            information = f.readlines()
            if information:
                print("Records about all employees:")
                for info in information:
                    print(info.strip())
            else:
                print("There is no any information about employees")

    except FileNotFoundError:
        print("There is no file named \' employees.txt \', sorry try again :)")

# Search for an employee by Employee ID
def search_employee(employee_file):
    search_id = input("Please, enter Employee ID here: ")
    try:
        with open(employee_file, "r") as f:
            list_employees = f.readlines()
            for search in list_employees:
                if search.startswith(search_id):
                    print('Here is the all info about employee you have searched: ', search.strip())

    except FileNotFoundError:
        print("There is no file named \' employees.txt \', sorry try again :)")

# Update an employee’s information (name, position, or salary) based on the Employee ID.
def update_employee_info(employee_file):
    employee_id = input("Please, enter Employee ID to updaterecord: ")
    new_employee_id = []
    info = False

    try:
        with open(employee_file, "r") as f:
            infos = f.readlines()
            for search in infos:
                info = True
                if search.startswith(employee_id):
                    print("Current info about an employee: ", search.strip())
                    new_employee_name = input("Input new name, please:" )
                    new_employee_position = input("Please, input an employee's new position: ")
                    new_employee_salary = input("Please, input the new salary for an employee: ")
                    new_employee_id.append(f"{employee_id}, {new_employee_name}, {new_employee_position}, {new_employee_salary} \n")

                else:
                    new_employee_id.append(search)
        
        if info:
            with open(employee_file, "w") as f:
                f.writelines(new_employee_id)
                print("Task done. All records updated.")
        else:
            print("Sorry, we couldn't find the employee you gave searched. ")

    except FileNotFoundError:
        print("There is no file named \' employees.txt \', sorry try again :)")

# Delete an employee's record from the file using the Employee ID.
def delete_info(employee_file):
    employee_id = input("Please, enter the Employee ID to delete: ")
    updated_info = []
    info = False

    try:
        with open(employee_file, "r") as f:
            infos = f.readlines()
            for search in infos:
                if search.startswith(employee_id):
                    info = True
                    continue # deleting records
                updated_info.append(search)
        if info:
            with open(employee_file, "w") as f:
                f.writelines(updated_info)
                print("All info belongs to an employee deleted")
        else:
            print(f"Sorry, there is no employee with {employee_id}, please check it again.")

    except FileNotFoundError:
        print("There is no file named \' employees.txt \', sorry try again :)")

        
def main_program_run():
    employee_file = "employees.txt"
    while True:
        employee_record_list()
        program_run = input("Please, select the option you are willing to do: ")
        if program_run == "1":
            add_new_employee(employee_file)
        elif program_run == "2":
            view_employees_record(employee_file)
        elif program_run == "3":
            search_employee(employee_file) 
        elif program_run == "4":
            update_employee_info(employee_file)
        elif program_run == "5":
            delete_info(employee_file)
        elif program_run == "6":
            print("Exit")
            break
        else:
            print("Invalid option. Please try again")

main_program_run()

