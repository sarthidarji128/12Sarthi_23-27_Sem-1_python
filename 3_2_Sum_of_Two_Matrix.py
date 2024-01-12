# Get dimensions of the matrices from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Create empty matrices to store the elements
matrix1 = [[0 for _ in range(cols)] for _ in range(rows)]  # Use _ for unused loop variables
matrix2 = [[0 for _ in range(cols)] for _ in range(rows)]
result = [[0 for _ in range(cols)] for _ in range(rows)]

# Get elements of matrix1 from the user
print("Enter elements for matrix1:")
for i in range(rows):
  for j in range(cols):
    matrix1[i][j] = int(input(f"Enter element at ({i+1},{j+1}): "))

# Get elements of matrix2 from the user
print("Enter elements for matrix2:")
for i in range(rows):
  for j in range(cols):
    matrix2[i][j] = int(input(f"Enter element at ({i+1},{j+1}): "))

# Calculate the sum of corresponding elements in both matrices
for i in range(rows):
  for j in range(cols):
    result[i][j] = matrix1[i][j] + matrix2[i][j]

# Print the resulting matrix
print("Sum of matrices:")
for row in result:
  print(row)
