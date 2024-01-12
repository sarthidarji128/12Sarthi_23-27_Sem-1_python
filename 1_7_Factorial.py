def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

number = int(input("Enter a non-negative integer: "))
result = factorial(number)
print("The factorial of", number, "is", result)
