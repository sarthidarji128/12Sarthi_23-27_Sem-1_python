# Get the value of n from the user
n = int(input("Enter the value of n: "))

# Initialize the sum to 0
sum = 0

# Print a message indicating the first n natural numbers
print("First", n, "natural numbers:")

# Use a for loop to iterate from 1 to n
for i in range(1, n + 1):
  # Print the current number i within the loop
  print(i, end=" ")  # Print each number with a space

  # Add the current number i to the sum
  sum += i

# Print a new line after the numbers
print("\n")

# Print the final sum of the first n natural numbers
print("Sum of first", n, "natural numbers:", sum)
