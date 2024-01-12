class LU:
  """
  Represents a "LU" entity with a code and name.
  """

  def __init__(self, lu_code, lu_name):
    """
    Initializes a LU object with the given code and name.

    Args:
      lu_code (str): The LU code.
      lu_name (str): The LU name.
    """

    self.lu_code = lu_code
    self.lu_name = lu_name

  def display_lu_info(self):
    """
    Prints the LU information (code and name).
    """

    print("LU Code:", self.lu_code)
    print("LU Name:", self.lu_name)

class ITM:
  """
  Represents an "ITM" entity with a code and name.
  """

  def __init__(self, itm_code, itm_name):
    """
    Initializes an ITM object with the given code and name.

    Args:
      itm_code (str): The ITM code.
      itm_name (str): The ITM name.
    """

    self.itm_code = itm_code
    self.itm_name = itm_name

  def display_itm_info(self):
    """
    Prints the ITM information (code and name).
    """

    print("ITM Code:", self.itm_code)
    print("ITM Name:", self.itm_name)

class DerivedClass(LU, ITM):
  """
  Inherits from both LU and ITM classes, combining their attributes and methods.
  """

  def __init__(self, lu_code, lu_name, itm_code, itm_name, derived_info):
    """
    Initializes a DerivedClass object, calling both parent class constructors and setting its own attribute.

    Args:
      lu_code (str): The LU code.
      lu_name (str): The LU name.
      itm_code (str): The ITM code.
      itm_name (str): The ITM name.
      derived_info (str): Additional information specific to the derived class.
    """

    LU.__init__(self, lu_code, lu_name)
    ITM.__init__(self, itm_code, itm_name)
    self.derived_info = derived_info

  def display_derived_info(self):
    """
    Prints the derived information specific to this class.
    """

    print("Information:", self.derived_info)

# Create a DerivedClass object with specific data
derived_object = DerivedClass("001", "Marketing", "001", "Finance", "Thank you..")

# Call methods to display information from all levels of inheritance
derived_object.display_lu_info()
print()
derived_object.display_itm_info()
print()
derived_object.display_derived_info()
