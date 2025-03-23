import json
import csv
import os
from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime

class TaskStatus(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"

class Task:
    def __init__(self, task_id, title, description, due_date=None, status=TaskStatus.PENDING):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status.value}"

    def to_dict(self):
        """Convert task to a dictionary for serialization."""
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status.value
        }

class TaskStorage(ABC):
    @abstractmethod
    def load_tasks(self):
        pass

    @abstractmethod
    def save_tasks(self, tasks):
        pass

class JSONStorage(TaskStorage):
    def __init__(self, filename):
        self.filename = filename

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as file:
            return [Task(**data) for data in json.load(file)]

    def save_tasks(self, tasks):
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)

class CSVStorage(TaskStorage):
    def __init__(self, filename):
        self.filename = filename

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as file:
            reader = csv.DictReader(file)
            return [Task(**row) for row in reader]

    def save_tasks(self, tasks):
        with open(self.filename, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["task_id", "title", "description", "due_date", "status"])
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

class TaskManager:
    def __init__(self, storage: TaskStorage):
        self.storage = storage
        self.tasks = self.storage.load_tasks()

    def add_task(self, task_id, title, description, due_date=None, status=TaskStatus.PENDING):
        task = Task(task_id, title, description, due_date, status)
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for task in self.tasks:
                print(task)

    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        for task in self.tasks:
            if task.task_id == task_id:
                if title:
                    task.title = title
                if description:
                    task.description = description
                if due_date:
                    task.due_date = due_date
                if status and status in TaskStatus.__members__:
                    task.status = TaskStatus[status]
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self, status):
        if status in TaskStatus.__members__:
            filtered_tasks = [task for task in self.tasks if task.status == TaskStatus[status]]
            if not filtered_tasks:
                print(f"No tasks found with status '{status}'.")
            else:
                print(f"Tasks with status '{status}':")
                for task in filtered_tasks:
                    print(task)
        else:
            print("Invalid status.")

    def save_tasks(self):
        self.storage.save_tasks(self.tasks)
        print("Tasks saved successfully!")

def main():
    print("Welcome to the To-Do Application!")
    print("Choose file format for storage: 1. JSON 2. CSV")
    format_choice = input("Enter your choice: ")

    if format_choice == "1":
        storage = JSONStorage("tasks.json")
    elif format_choice == "2":
        storage = CSVStorage("tasks.csv")
    else:
        print("Invalid choice. Exiting.")
        return

    manager = TaskManager(storage)

    while True:
        print("\n1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Load tasks")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (YYYY-MM-DD, leave blank if not applicable): ")
            status = input("Enter Status (Pending/In Progress/Completed): ")
            manager.add_task(task_id, title, description, due_date if due_date else None, TaskStatus[status.upper()] if status.upper() in TaskStatus.__members__ else TaskStatus.PENDING)
        
        elif choice == "2":
            manager.view_tasks()
        
        elif choice == "3":
            task_id = input("Enter Task ID to update: ")
            title = input("Enter new Title (leave blank to keep current): ")
            description = input("Enter new Description (leave blank to keep current): ")
            due_date = input("Enter new Due Date (leave blank to keep current): ")
            status = input("Enter new Status (leave blank to keep current): ")
            manager.update_task(task_id, title if title else None, description if description else None, due_date if due_date else None, status if status else None)
        
        elif choice == "4":
            task_id = input("Enter Task ID to delete: ")
            manager.delete_task(task_id)
        
        elif choice == "5":
            status = input("Enter status to filter by (Pending/In Progress/Completed): ")
            manager.filter_tasks(status.upper())
        
        elif choice == "6":
            manager.save_tasks()
        
        elif choice == "7":
            manager.tasks = manager.storage.load_tasks()
            print("Tasks loaded successfully!")
        
        elif choice == "8":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()