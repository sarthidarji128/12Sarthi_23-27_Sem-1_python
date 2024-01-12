# Create a list of numbers
a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Print the complete list
print("Complete list:", a)
print()

# Accessing elements:
print("Fourth element:", a[3])  # Accessing by index
print()
print("List from 0th to 4th index:", a[:4])  # Slicing to get elements from index 0 to 3
print()
print("List from -7th to 3rd element:", a[-7:3])  # Slicing from index -7 to 2 (not including 3)
print()

# Modifying the list:
a.append(110)  # Adding an element to the end
print("List after appending 110:", a)
print()
a.sort()  # Sorting the list in ascending order
print("Sorted list:", a)
print()

# Removing elements:
element = a.pop()  # Removing and returning the last element
print("Popped element:", element)
print("List after popping:", a)
print()
a.remove(60)  # Removing the first occurrence of 60
print("List after removing 60:", a)
print()

# Inserting elements:
a.insert(2, 45)  # Inserting 45 at index 2
print("List after inserting 45 at index 2:", a)
print()

# Counting elements:
count = a.count(30)  # Counting the occurrences of 30
print("Occurrence of 30 in the list:", count)
print()

# Extending the list:
a.extend([120, 130])  # Adding multiple elements at the end
print("List after extending:", a)
print()

# Reversing the list:
a.reverse()  # Reversing the order of elements
print("List after reversing:", a)
