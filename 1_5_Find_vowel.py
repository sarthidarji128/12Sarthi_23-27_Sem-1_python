# Define a string containing all vowels (both lowercase and uppercase)
vowels = "aeiouAEIOU"

# Prompt the user to enter a character
character = input("Enter a character: ")

# Check if the entered character is a vowel using the "in" operator
if character in vowels:  # True if the character is found within the vowels string
  print(character, "is a vowel.")  # Print a message indicating the character is a vowel
else:  # False if the character is not found in the vowels string
  print(character, "is not a vowel.")  # Print a message indicating the character is not a vowel
