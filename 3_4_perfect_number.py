def is_perfect_number(n):
  """
  Checks if a number is a perfect number.

  A perfect number is a positive integer that is equal to the sum of its proper divisors
  (excluding itself).

  Args:
    n: The integer to be checked.

  Returns:
    True if the number is a perfect number, False otherwise.
  """

  # Find all divisors of the number except 1 and itself
  divisors = [i for i in range(2, n) if n % i == 0]

  # Calculate the sum of the divisors
  sum_of_divisors = sum(divisors)

  # Check if the sum of divisors is equal to the number itself
  return sum_of_divisors == n

# Get a number from the user
number = int(input("Enter a number: "))

# Check if the number is perfect using the function
if is_perfect_number(number):
  print(number, "is a perfect number.")
else:
  print(number, "is not a perfect number.")
