def get_distinct_elements_set(input_list):
  """
  Removes duplicate elements from a list using a set.

  Args:
    input_list: The list to remove duplicates from.

  Returns:
    A list containing only the unique elements from the input list.
  """

  distinct_set = set(input_list)  # Create a set to automatically remove duplicates
  return list(distinct_set)  # Convert back to a list and return

def get_distinct_elements_loop(input_list):
  """
  Removes duplicate elements from a list using a loop and a set for tracking.

  Args:
    input_list: The list to remove duplicates from.

  Returns:
    A list containing only the unique elements from the input list.
  """

  distinct_list = []  # Initialize an empty list to store distinct elements
  seen = set()  # Create a set to keep track of seen elements

  for item in input_list:
    if item not in seen:  # Check if the item is already seen
      distinct_list.append(item)  # If not seen, add it to the distinct list
      seen.add(item)  # Mark it as seen in the set

  return distinct_list  # Return the list of distinct elements

def get_distinct_elements_user_input():
  """
  Prompts the user for a list of numbers, removes duplicates, and prints the result.
  """

  input_str = input("Enter a list of numbers separated by spaces: ")
  input_list = []

  for num_str in input_str.split():  # Split the input string into numbers
    input_list.append(int(num_str))  # Convert each number to an integer and add to list

  distinct_list = get_distinct_elements_set(input_list)  # Get distinct elements using set method
  print("Distinct elements:", distinct_list)  # Print the result

# Call the function to get input and process distinct elements
get_distinct_elements_user_input()
