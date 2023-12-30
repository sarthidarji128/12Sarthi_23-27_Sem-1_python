class Number:
    def get_numbers(self):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2

class Adder(Number):
    def add(self):
        num1, num2 = self.get_numbers()  
        result = num1 + num2
        print("The sum of the numbers is:", result)

adder = Adder()
adder.add()
