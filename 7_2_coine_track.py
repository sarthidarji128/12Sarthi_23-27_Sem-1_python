API_KEY = 'CG-Kjmr47XUisC8wTQ75jsf7wAS'  # Your CoinGecko API key
import requests  # Library for making HTTP requests

while True:
    coin = input("Enter cryptocoin: ")  # Prompt user for a cryptocoin name

    # Make a request to the CoinGecko API to get the price
    response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd,inr&x_cg_demo_api_key={API_KEY}")

    a = response.json()  # Parse the JSON response

    if coin in a:  # Check if the requested coin is found in the response
        print(a)  # Print the full JSON response (optional for debugging)
        print("\nCrypto:", coin)  # Print the coin name
        print("Price:", a[coin]['usd'], "USD")  # Print the price in USD
        print("Price:", a[coin]['inr'], "INR")  # Print the price in INR

    else:
        print("Invalid cryptocoin!")  # Error message for invalid coin

    # Ask if the user wants to see more cryptocoins
    b = input("Want to see more cryptocoins?(y/n):")
    if b.lower() == "n":
        break  # Exit the loop if user wants to stop
