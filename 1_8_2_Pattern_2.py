# Get the number of rows from the user
n = int(input("Enter the value of rows: "))

# Use a loop to print the right-angled triangle pattern
for i in range(1, n + 1):  # Iterate from 1 to n (inclusive)
  print(str(i) * i + " " * (n + 1 - i))  # Print i copies of the current number followed by spaces
