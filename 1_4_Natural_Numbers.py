n = int(input("Enter the value of n: "))
sum = 0
print("First", n, "natural numbers:")
for i in range(1, n + 1):
   print(i,end=" ")
   sum =sum+i

print("\nSum of first", n, "natural numbers:", sum)
