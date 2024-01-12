class Number:
  """
  Provides a basic foundation for working with numbers, primarily getting user input.
  """

  def get_numbers(self):
    """
    Prompts the user to enter two numbers and returns them as a tuple.

    Returns:
      A tuple containing the two numbers as floats.
    """

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1, num2

class Adder(Number):
  """
  Inherits from the Number class and adds the ability to perform addition.
  """

  def add(self):
    """
    Gets two numbers from the user, adds them, and prints the result.
    """

    num1, num2 = self.get_numbers()  # Inherits the get_numbers() method
    result = num1 + num2
    print("The sum of the numbers is:", result)

# Create an Adder object and call its add() method
adder = Adder()
adder.add()
