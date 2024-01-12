# Get the number of rows from the user
n = int(input("Enter the number of rows: "))

# Use a loop to print the pyramid pattern
for i in range(1, n):  # Iterate from 1 to n-1 (inclusive)
  print("*" * i)  # Print i asterisks in each row
