# Get the number of rows from the user
n = int(input("Enter the value of rows: "))

# Use a loop to print the right-angled triangle pattern
for i in range(1, n):  # Iterate from 1 to n-1 (inclusive)
  print(" " * (n - i) + "*" * (2 * i - 1))  # Print spaces and asterisks for each row
