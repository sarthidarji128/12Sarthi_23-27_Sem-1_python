class LibraryItem:
  """
  Represents a generic library item with basic attributes and check-out/check-in functionality.
  """

  def __init__(self, title, author):
    """
    Initializes a LibraryItem object with the given title and author.

    Args:
      title (str): The title of the item.
      author (str): The author or creator of the item.
    """

    self.title = title
    self.author = author
    self.is_checked_out = False  # Tracks the item's check-out status

  def check_out(self):
    """
    Checks out the item, updating its status if it's not already checked out.
    """

    if self.is_checked_out:
      print("Item is already checked out.")
    else:
      self.is_checked_out = True
      print("Item checked out successfully.")

  def check_in(self):
    """
    Checks in the item, updating its status if it's currently checked out.
    """

    if not self.is_checked_out:
      print("Item is already checked in.")
    else:
      self.is_checked_out = False
      print("Item checked in successfully.")

class Book(LibraryItem):
  """
  Represents a book, inheriting from LibraryItem and adding an ISBN.
  """

  def __init__(self, title, author, isbn):
    """
    Initializes a Book object, calling the LibraryItem constructor and adding the ISBN.

    Args:
      title (str): The title of the book.
      author (str): The author of the book.
      isbn (str): The ISBN of the book.
    """

    super().__init__(title, author)  # Call the LibraryItem constructor
    self.isbn = isbn

class DVD(LibraryItem):
  """
  Represents a DVD, inheriting from LibraryItem and adding a release year.
  """

  def __init__(self, title, director, release_year):
    """
    Initializes a DVD object, calling the LibraryItem constructor and adding the release year.

    Args:
      title (str): The title of the DVD.
      director (str): The director of the DVD.
      release_year (int): The release year of the DVD.
    """

    super().__init__(title, director)  # Call the LibraryItem constructor
    self.release_year = release_year

class Journal(LibraryItem):
  """
  Represents a journal, inheriting from LibraryItem and adding an issue number.
  """

  def __init__(self, title, publisher, issue_number):
    """
    Initializes a Journal object, calling the LibraryItem constructor and adding the issue number.

    Args:
      title (str): The title of the journal.
      publisher (str): The publisher of the journal.
      issue_number (int): The issue number of the journal.
    """

    super().__init__(title, publisher)  # Call the LibraryItem constructor
    self.issue_number = issue_number
