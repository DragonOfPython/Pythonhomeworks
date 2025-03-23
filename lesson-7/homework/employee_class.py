import json
import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

    def to_dict(self):
        """Convert the employee to a dictionary for easy JSON serialization."""
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "position": self.position,
            "salary": self.salary
        }

class EmployeeManager:
    def __init__(self, filename="employees.json"):
        self.filename = filename
        self.load_employees()

    def load_employees(self):
        """Load employees from the JSON file."""
        self.employees = {}
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                data = json.load(file)
                for emp_data in data:
                    emp = Employee(emp_data["employee_id"], emp_data["name"], emp_data["position"], emp_data["salary"])
                    self.employees[emp.employee_id] = emp

    def save_employees(self):
        """Save employees to the JSON file."""
        with open(self.filename, "w") as file:
            json.dump([emp.to_dict() for emp in self.employees.values()], file, indent=4)

    def add_employee(self, employee_id, name, position, salary):
        """Add a new employee."""
        if employee_id in self.employees:
            print("Error: Employee ID already exists.")
        else:
            self.employees[employee_id] = Employee(employee_id, name, position, salary)
            self.save_employees()
            print("Employee added successfully!")

    def view_all_employees(self):
        """View all employee records."""
        if not self.employees:
            print("No employee records found.")
        else:
            print("Employee Records:")
            for employee in self.employees.values():
                print(employee)

    def search_employee(self, employee_id):
        """Search for an employee by Employee ID."""
        employee = self.employees.get(employee_id)
        if employee:
            print("Employee Found:")
            print(employee)
        else:
            print("Employee not found.")

    def update_employee(self, employee_id, name=None, position=None, salary=None):
        """Update an employee's information."""
        employee = self.employees.get(employee_id)
        if not employee:
            print("Error: Employee not found.")
            return
        
        if name:
            employee.name = name
        if position:
            employee.position = position
        if salary is not None:
            employee.salary = salary
        
        self.save_employees()
        print("Employee information updated successfully!")

    def delete_employee(self, employee_id):
        """Delete an employee by Employee ID."""
        if employee_id in self.employees:
            del self.employees[employee_id]
            self.save_employees()
            print("Employee deleted successfully!")
        else:
            print("Error: Employee not found.")

def main():
    manager = EmployeeManager()
    
    while True:
        print("\nWelcome to the Employee Records Manager!")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            employee_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            position = input("Enter Position: ")
            salary = float(input("Enter Salary: "))
            manager.add_employee(employee_id, name, position, salary)
        
        elif choice == "2":
            manager.view_all_employees()
        
        elif choice == "3":
            employee_id = input("Enter Employee ID to search: ")
            manager.search_employee(employee_id)
        
        elif choice == "4":
            employee_id = input("Enter Employee ID to update: ")
            name = input("Enter new Name (leave blank to keep current): ")
            position = input("Enter new Position (leave blank to keep current): ")
            salary_input = input("Enter new Salary (leave blank to keep current): ")
            salary = float(salary_input) if salary_input else None
            manager.update_employee(employee_id, name if name else None, position if position else None, salary)
        
        elif choice == "5":
            employee_id = input("Enter Employee ID to delete: ")
            manager.delete_employee(employee_id)
        
        elif choice == "6":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()