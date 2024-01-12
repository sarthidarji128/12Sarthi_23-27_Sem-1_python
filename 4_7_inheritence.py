class Grandfather:
  """
  Represents a grandfather with a house and a car.
  """

  def __init__(self, house, car):
    """
    Initializes a Grandfather object with the given house and car.

    Args:
      house (str): The grandfather's house.
      car (str): The grandfather's car.
    """

    self.house = house
    self.car = car

class Father(Grandfather):
  """
  Represents a father who inherits from Grandfather and has additional land.
  """

  def __init__(self, house, car, land):
    """
    Initializes a Father object, calling the Grandfather constructor and adding land.

    Args:
      house (str): The father's house (inherited from Grandfather).
      car (str): The father's car (inherited from Grandfather).
      land (str): The father's land.
    """

    super().__init__(house, car)  # Call the Grandfather constructor
    self.land = land

class Child(Father):
  """
  Represents a child who inherits from Father and has additional savings.
  """

  def __init__(self, house, car, land, savings):
    """
    Initializes a Child object, calling the Father constructor and adding savings.

    Args:
      house (str): The child's house (inherited from Father and Grandfather).
      car (str): The child's car (inherited from Father and Grandfather).
      land (str): The child's land (inherited from Father).
      savings (int): The child's savings.
    """

    super().__init__(house, car, land)  # Call the Father constructor
    self.savings = savings

# Create a Child object with specific assets
child = Child("mansion", "luxury car & bike & tracktor", "farm & 49 bhega Land", 100000)

# Access and print all inherited and child-specific assets
print(f"House: {child.house}")  # Inherited from Grandfather
print(f"Car: {child.car}")  # Inherited from Grandfather
print(f"Land: {child.land}")  # Inherited from Father
print(f"Savings: {child.savings} ₹")  # Specific to Child
