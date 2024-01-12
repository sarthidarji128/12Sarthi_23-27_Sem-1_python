import mymod  # Import the module named 'mymod'

# Get user input for numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Call the add_numbers function from the imported module
result = mymod.add_numbers(num1, num2)

# Print the calculated sum
print("The sum of", num1, "and", num2, "is", result)
