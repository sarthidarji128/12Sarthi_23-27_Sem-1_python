def count_upper_lower(string):
  """
  Counts the number of uppercase and lowercase letters in a string.

  Args:
    string: The string to analyze.

  Returns:
    A tuple containing the number of uppercase letters and the number of lowercase letters.
  """

  uppercase_count = 0  # Initialize a counter for uppercase letters
  lowercase_count = 0  # Initialize a counter for lowercase letters

  for char in string:  # Loop through each character in the string
    if char.isupper():  # Check if the character is uppercase
      uppercase_count += 1  # Increment the uppercase counter
    elif char.islower():  # Check if the character is lowercase
      lowercase_count += 1  # Increment the lowercase counter

  return uppercase_count, lowercase_count  # Return the counts as a tuple

# Example usage
string_test = "Today is My Best Day"
uppercase_count, lowercase_count = count_upper_lower(string_test)

print("Number of uppercase letters:", uppercase_count)
print("Number of lowercase letters:", lowercase_count)
