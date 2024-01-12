class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        if self.is_checked_out:
            print("Item is already checked out.")
        else:
            self.is_checked_out = True
            print("Item checked out successfully.")

    def check_in(self):
        if not self.is_checked_out:
            print("Item is already checked in.")
        else:
            self.is_checked_out = False
            print("Item checked in successfully.")

class Book(LibraryItem):
    def __init__(self, title, author, isbn):
        super().__init__(title, author)
        self.isbn = isbn

class DVD(LibraryItem):
    def __init__(self, title, director, release_year):
        super().__init__(title, director)
        self.release_year = release_year

class Journal(LibraryItem):
    def __init__(self, title, publisher, issue_number):
        super().__init__(title, publisher)
        self.issue_number = issue_number

# Example usage:
book = Book("The Lord of the Rings", "J.R.R. Tolkien", "9780547928227")
dvd = DVD("The Matrix", "The Wachowskis", 1999)
journal = Journal("Nature", "Springer Nature", 554)

# Check out items
book.check_out()
print(book.author)
dvd.check_in() 
print(dvd.author)
# Check in items
book.check_in()
print(journal.author)
journal.check_out()
