def get_user_info(*args, **kwargs):
  """
  Gets user information using a flexible combination of positional and keyword arguments.

  Args:
    *args: A tuple of positional arguments to capture name and email.
    **kwargs: A dictionary of keyword arguments to capture optional information like age.

  Returns:
    A tuple containing the name, email, and age (if provided).
  """

  name = args[0]  # Extract name from the first positional argument
  email = args[1]  # Extract email from the second positional argument
  age = kwargs.get("age")  # Get age from keyword arguments, if provided

  return name, email, age  # Return the extracted information

# Get user input for name, email, and age
name = input("Enter your name: ")
email = input("Enter your email: ")
age = input("Enter your age: ")

# Call the function with positional and keyword arguments
name, email, age = get_user_info(name, email, age=age)

# Print the retrieved information
print("Name:", name)
print("Email:", email)
print("Age:", age)
