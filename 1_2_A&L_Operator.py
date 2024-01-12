# This program demonstrates arithmetic and relational operators in Python.

# Get input for two numbers from the user
num1 = float(input("Enter first number: "))  # Store the first number as a floating-point value
num2 = float(input("Enter second number: "))  # Store the second number as a floating-point value

# Perform arithmetic operations and print the results:
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2, "(quotient)")  # Regular division, resulting in a floating-point quotient
print("Floor Division:", num1 // num2, "(rounded down)")  # Integer division, discarding any remainder
print("Modulus (remainder):", num1 % num2)  # Remainder after division
print("Exponentiation:", num1 ** num2)  # num1 raised to the power of num2

# Perform relational comparisons and print the results (True or False):
print("num1 > num2:", num1 > num2)  # Check if num1 is greater than num2
print("num1 < num2:", num1 < num2)  # Check if num1 is less than num2
print("num1 >= num2:", num1 >= num2)  # Check if num1 is greater than or equal to num2
print("num1 <= num2:", num1 <= num2)  # Check if num1 is less than or equal to num2
print("num1 == num2:", num1 == num2)  # Check if num1 is equal to num2
print("num1 != num2:", num1 != num2)  # Check if num1 is not equal to num2
