class Student:
    total_students = 0

    def __init__(self, name, department):
        self.name = name
        self.department = department
        Student.total_students += 1

    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Department: {self.department}")
        print()

# Example usage:
# Create instances of Student class for different students
student1 = Student(name="xyz ", department="PGDM")
student2 = Student(name="sarthi", department="BTech")
student3 = Student(name="Darji", department="BTech")

# Display details of each student
print("Details of Admitted Students:")
student1.display_details()
student2.display_details()
student3.display_details()

# Display the total number of students
print(f"Total Students Admitted: {Student.total_students}")