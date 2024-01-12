def is_armstrong(n):
  """
  This function checks if a number is an Armstrong number.

  Args:
    n: The number to be checked.

  Returns:
    True if the number is an Armstrong number, False otherwise.
  """

  # Store the original number for later comparison
  original_num = n

  # Initialize a variable to store the sum of digits raised to their number of digits
  sum_of_digits = 0

  # Loop through each digit of the number
  while n > 0:
    # Extract the last digit using modulo operator
    digit = n % 10

    # Add the digit raised to the power of the number of digits in the original number
    sum_of_digits += digit**len(str(original_num))

    # Divide the number by 10 to move to the next digit
    n //= 10

  # Check if the sum of digits raised to their powers is equal to the original number
  return sum_of_digits == original_num

# Example usage
number = int(input("Enter a number to check if it's an Armstrong number: "))

if is_armstrong(number):
  print(f"{number} is an Armstrong number.")
else:
  print(f"{number} is not an Armstrong number.")
