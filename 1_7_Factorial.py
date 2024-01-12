def factorial(n):
  """
  This function calculates the factorial of a non-negative integer.

  Args:
    n: The non-negative integer for which to calculate the factorial.

  Returns:
    The factorial of n, or an error message if n is negative.
  """

  if n < 0:
    return "Factorial is not defined for negative numbers."  # Handle negative input
  elif n == 0:
    return 1  # Base case: factorial of 0 is 1
  else:
    factorial = 1  # Initialize a variable to store the factorial
    for i in range(1, n + 1):  # Iterate from 1 to n
      factorial *= i  # Multiply factorial by each number in the range
    return factorial  # Return the calculated factorial

# Example usage
number = int(input("Enter a non-negative integer: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")
