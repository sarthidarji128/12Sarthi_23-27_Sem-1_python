def domainn(email):
  """
  Extracts the username and domain from an email address.

  Args:
    email: The email address to parse.

  Returns:
    A tuple containing the username and domain, or None if the email is invalid.
  """

  index = email.find("@")  # Find the index of the "@" symbol
  if index != -1:  # Check if "@" is present in the email
    username = email[:index]  # Extract username (part before "@")
    domain = email[index + 1:]  # Extract domain (part after "@")
    return username, domain  # Return both as a tuple
  else:
    print("Error: Invalid email address.")  # Handle invalid email
    return None  # Return None to indicate invalid email

# Get an email address from the user
email = input("Enter an email address: ")

# Extract username and domain using the function
username, domain = domainn(email)

# Check if valid username and domain were extracted
if username and domain:
  print("Username:", username)
  print("Domain:", domain)
else:
  print("Invalid email address.")
