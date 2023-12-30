def is_armstrong(n):
    original_num = n
    sum_of_digits = 0
    while n > 0:
        digit = n % 10
        sum_of_digits =sum_of_digits+ digit**len(str(original_num))
        n //= 10
    return sum_of_digits == original_num

number = int(input("Enter a number to check if it's an Armstrong number: "))

if is_armstrong(number):
  print(number ,"is an Armstrong number.")
else:
  print(number ,"is not an Armstrong number.")
 