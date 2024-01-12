# Get the principal amount from the user
principal = float(input("Enter the principal amount: "))

# Get the annual interest rate from the user
rate = float(input("Enter the rate of interest per annum: "))

# Get the time period in years from the user
time = float(input("Enter the time period in years: "))

# Calculate the simple interest using the formula
simple_interest = (principal * rate * time) / 100

# Print the calculated simple interest
print("Simple Interest: ₹", simple_interest)

# Calculate the total amount by adding the principal and simple interest
total_amount = simple_interest + principal

# Print the total amount
print("Total Amount : ₹", total_amount)
