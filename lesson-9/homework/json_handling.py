import json
import csv

class TaskManager:
    """Class to manage tasks loaded from a JSON file."""
    def __init__(self, json_file):
        self.json_file = json_file
        self.tasks = []

    def load_tasks(self):
        """Load tasks from the JSON file."""
        try:
            with open(self.json_file, 'r') as file:
                self.tasks = json.load(file)
                print(f"Loaded {len(self.tasks)} tasks from '{self.json_file}'.")  # Debugging output
        except FileNotFoundError:
            print(f"Error: The file '{self.json_file}' does not exist.")
        except json.JSONDecodeError:
            print("Error: Failed to parse JSON from the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def display_tasks(self):
        """Display all tasks."""
        print(f"{'ID':<5} {'Task Name':<20} {'Completed':<10} {'Priority':<10}")
        for task in self.tasks:
            print(f"{task['id']:<5} {task['task']:<20} {str(task['completed']):<10} {task['priority']:<10}")

    def calculate_statistics(self):
        """Calculate and return task completion statistics."""
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task['completed'])
        pending_tasks = total_tasks - completed_tasks
        average_priority = sum(task['priority'] for task in self.tasks) / total_tasks if total_tasks > 0 else 0
        
        return {
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'pending_tasks': pending_tasks,
            'average_priority': average_priority
        }

    def save_tasks(self):
        """Save any changes back to the JSON file."""
        try:
            with open(self.json_file, 'w') as file:
                json.dump(self.tasks, file, indent=4)
            print(f"Tasks saved back to '{self.json_file}'.")  # Debugging output
        except Exception as e:
            print(f"Error writing to file: {e}")

    def convert_to_csv(self, csv_file):
        """Convert the tasks to a CSV file."""
        try:
            with open(csv_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['ID', 'Task', 'Completed', 'Priority'])  # Write header
                for task in self.tasks:
                    writer.writerow([task['id'], task['task'], task['completed'], task['priority']])
            print(f"Tasks have been converted to '{csv_file}'.")  # Debugging output
        except Exception as e:
            print(f"Error writing to CSV file: {e}")

if __name__ == "__main__":
    # Create a TaskManager instance
    task_manager = TaskManager('tasks.json')

    # Load tasks from the JSON file
    task_manager.load_tasks()
    
    # Display all tasks
    task_manager.display_tasks()

    # Calculate and display statistics
    stats = task_manager.calculate_statistics()
    print("\nTask Completion Statistics:")
    print(f"Total tasks: {stats['total_tasks']}")
    print(f"Completed tasks: {stats['completed_tasks']}")
    print(f"Pending tasks: {stats['pending_tasks']}")
    print(f"Average priority: {stats['average_priority']:.2f}")

    # Save tasks back to the JSON file (if any modifications were made)
    task_manager.save_tasks()

    # Convert tasks to a CSV file
    task_manager.convert_to_csv('tasks.csv')