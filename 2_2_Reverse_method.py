# Reverse a list using the `reverse` method
my_list1 = [11, 22, 33, 44, 55]
my_list1.reverse()  # Reverse the elements of the list in-place

print("Reverse using `reverse` method:")
for item in my_list1:
    print(item, end=" ")
print()  # Print a newline

# Reverse a list using slicing
my_list2 = [13, 32, 53, 74, 95]

print("Reverse using slicing:")
for item in my_list2[::-1]:  # Iterate through the reversed list using slicing
    print(item, end=" ")
