# Define a list of BRICS countries
brics_countries = ["Brazil", "Russia", "India", "China", "South Africa"]

# Get a country name from the user
country_name = str(input("Enter a country name: "))

# Check if the entered country is in the BRICS list
if country_name in brics_countries:  # Use the "in" operator to check membership
  print(country_name, "is a member of BRICS.")
else:
  print(country_name, "is not a member of BRICS.")
