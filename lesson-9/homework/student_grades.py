import csv
from collections import defaultdict, namedtuple

class GradeEntry:
    """Class to represent a single grade entry."""
    def __init__(self, name, subject, grade):
        self.name = name
        self.subject = subject
        self.grade = grade

class GradeManager:
    """Class to manage grades, including reading, calculating averages, and writing to CSV."""
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.grades = []

    def read_grades(self):
        """Read grades from a CSV file and store them as GradeEntry objects."""
        try:
            with open(self.input_file, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.grades.append(GradeEntry(
                        name=row['Name'],
                        subject=row['Subject'],
                        grade=float(row['Grade'])  # Convert grade to float
                    ))
        except FileNotFoundError:
            print(f"Error: The file '{self.input_file}' does not exist.")
        except ValueError as e:
            print(f"Error processing data: {e}")

    def calculate_average_grades(self):
        """Calculate average grades for each subject."""
        subject_totals = defaultdict(float)
        subject_counts = defaultdict(int)

        for entry in self.grades:
            subject = entry.subject
            grade = entry.grade
            subject_totals[subject] += grade
            subject_counts[subject] += 1

        return {subject: subject_totals[subject] / subject_counts[subject] for subject in subject_totals}

    def write_average_grades(self, average_grades):
        """Write average grades to a new CSV file."""
        try:
            with open(self.output_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Subject', 'Average Grade'])  # Write header
                for subject, average in average_grades.items():
                    writer.writerow([subject, round(average, 2)])  # Round to 2 decimal places
        except Exception as e:
            print(f"Error writing to file: {e}")

if __name__ == "__main__":
    # Create a GradeManager instance
    grade_manager = GradeManager('grades.csv', 'average_grades.csv')
    
    # Read grades from the CSV file
    grade_manager.read_grades()
    
    # Calculate average grades for each subject
    average_grades = grade_manager.calculate_average_grades()
    
    # Write the average grades to a new CSV file
    grade_manager.write_average_grades(average_grades)

    print("Average grades have been calculated and saved to 'average_grades.csv'.")