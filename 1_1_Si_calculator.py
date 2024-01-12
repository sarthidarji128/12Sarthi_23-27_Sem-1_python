principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest per annum: "))
time = float(input("Enter the time period in years: "))
simple_interest = (principal * rate * time) / 100
print("Simple Interest: ₹", simple_interest)
print("Total Amount : ₹", simple_interest+principal)
