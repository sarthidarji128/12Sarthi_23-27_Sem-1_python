def a(n):
  divisors = [i for i in range(1, n) if n % i == 0]
  sum_of_divisors = sum(divisors)
  return sum_of_divisors == n


number = int(input("Enter a number: "))
if a(number):
  print(number," is a perfect number.")
else:
  print(number," is not a perfect number.")
