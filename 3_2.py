rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print("Enter elements for matrix1:")
matrix1 = [[int(input(f"Enter element at ({i+1},{j+1}): ")) for j in range(cols)] for i in range(rows)]

print("Enter elements for matrix2:")
matrix2 = [[int(input(f"Enter element at ({i+1},{j+1}): ")) for j in range(cols)] for i in range(rows)]

result = [[0 for s in range(cols)] for s in range(rows)]


for i in range(rows):
  for j in range(cols):
    result[i][j] = matrix1[i][j] + matrix2[i][j]


print("Sum of matrices:")
for row in result:
  print(row)
