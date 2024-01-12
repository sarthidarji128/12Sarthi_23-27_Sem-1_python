class Employee:
    def __init__(self, name, age, department, salary):

        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def get_details(self):
        
        return {
            "name": self.name,
            "age": self.age,
            "department": self.department,
            "salary": self.salary,
        }

    def print_details(self):

        print("Name:", self.name)
        print("Age: ",self.age)
        print("Department: ",self.department)
        print("Salary: $",self.salary)


emp1 = Employee("Sarthi Darji", 17, "Finance", 5000000)
emp2 = Employee("Jeevan Anaa", 19, "Marketing", 450000)
emp3=Employee("Lachh bahi",20 ,"Finance",99999)

employee1_details = emp1.get_details()
print("Employee 1 details: ",employee1_details)
print()
employee2_details = emp2.get_details()
print("Employee 2 details: ",employee2_details)
print()
employee3_details = emp3.get_details()
print("Employee 3 details: ",employee3_details)
