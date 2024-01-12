n=int(input("Enter the value of rows :"))
for i in range(1, n):
      print(" " * (n - i) + "*" * (2 * i - 1))
