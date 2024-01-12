# Prompt the user to enter a number
number = int(input("Enter a number: "))  # Convert the input to an integer

# Check if the number is even or odd using the modulo operator
if number % 2 == 0:  # True if the remainder after dividing by 2 is 0 (even)
  print(number, "is even.")  # Print a message indicating the number is even
else:  # False if the remainder is not 0 (odd)
  print(number, "is odd.")  # Print a message indicating the number is odd
