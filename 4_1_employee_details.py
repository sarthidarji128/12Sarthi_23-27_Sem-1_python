class Employee:
  """
  Represents an employee with attributes like name, age, department, and salary.
  """

  def __init__(self, name, age, department, salary):
    """
    Initializes an Employee object with the given attributes.

    Args:
      name (str): Name of the employee.
      age (int): Age of the employee.
      department (str): Department the employee works in.
      salary (int): Salary of the employee.
    """

    self.name = name
    self.age = age
    self.department = department
    self.salary = salary

  def get_details(self):
    """
    Returns a dictionary containing the employee's details.

    Returns:
      dict: A dictionary with keys "name", "age", "department", and "salary".
    """

    return {
      "name": self.name,
      "age": self.age,
      "department": self.department,
      "salary": self.salary,
    }

  def print_details(self):
    """
    Prints the employee's details to the console.
    """

    print("Name:", self.name)
    print("Age:", self.age)
    print("Department:", self.department)
    print("Salary: $", self.salary)

# Create employee objects
emp1 = Employee("Sarthi Darji", 17, "Finance", 5000000)
emp2 = Employee("Jeevan Anaa", 19, "Marketing", 450000)
emp3 = Employee("Lachh bahi", 20, "Finance", 99999)

# Get and print employee details using both methods
employee1_details = emp1.get_details()
print("Employee 1 details (as dictionary): ", employee1_details)
print()
emp1.print_details()  # Print details directly
print()

employee2_details = emp2.get_details()
print("Employee 2 details (as dictionary): ", employee2_details)
print()
emp2.print_details()
print()

employee3_details = emp3.get_details()
print("Employee 3 details (as dictionary): ", employee3_details)
print()
emp3.print_details()
