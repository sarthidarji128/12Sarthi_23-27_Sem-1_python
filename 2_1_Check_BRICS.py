brics_countries = ["Brazil", "Russia", "India", "China", "South Africa"]
country_name = str(input("Enter a country name: "))
if country_name in brics_countries:
    print(country_name, "is a member of BRICS.")
else:
    print(country_name, "is not a member of BRICS.")
