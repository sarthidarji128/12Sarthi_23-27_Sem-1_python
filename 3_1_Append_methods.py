# Create a list with initial elements
a = [1, 2, 3]

# Extend using the + operator (creates a new list):
extended = a + [4, 5]  # Concatenates two lists to create a new one
print("Extended list using + operator:", extended)  # New list: [1, 2, 3, 4, 5]

# Extend using append() (modifies the original list):
a.append(6)  # Adds a single element to the end of the list
a.append(7)  # Adds another element
print("Extended list using append():", a)  # List a is now: [1, 2, 3, 6, 7]

# Extend using extend() (modifies the original list):
a.extend([8, 9])  # Adds multiple elements from another list to the end
print("Extended list using extend():", a)  # List a is now: [1, 2, 3, 6, 7, 8, 9]
