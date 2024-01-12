def cube_range(a, b):
  """
  Creates a dictionary containing cubes of odd numbers within a given range.

  Args:
    a: The starting number of the range (inclusive).
    b: The ending number of the range (inclusive).

  Returns:
    A dictionary where keys are odd numbers in the range and values are their cubes.
  """

  cubes = {}  # Create an empty dictionary to store cubes

  for num in range(a, b + 1):  # Iterate through numbers from a to b (inclusive)
    if num % 2 != 0:  # Check if the number is odd
      cubes[num] = num**3  # Calculate the cube and add it to the dictionary

  return cubes  # Return the dictionary of cubes

# Call the function with a range of 1 to 5
cubes = cube_range(1, 5)

# Print the resulting dictionary
print(cubes)
