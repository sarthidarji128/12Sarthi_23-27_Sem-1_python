a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("Complete list:", a)
print()
print("Fourth element:", a[3])
print()
print("List from 0th to 4th index:", a[:4])
print()
print("List from -7th to 3rd element:", a[-7:3])
print()
a.append(110)
print("List after appending 110:", a)
print()
a.sort()
print("Sorted list:", a)

print()
element = a.pop()
print("Popped element:", element)
print("List after popping:", a)
print()

a.remove(60)
print("List after removing 60:", a)
print()

a.insert(2, 45)
print("List after inserting 45 at index 2:", a)

print()
count = a.count(30)
print("Occurrence of 30 in the list:", count)

print()
a.extend([120, 130])
print("List after extending:", a)

print()
a.reverse()
print("List after reversing:", a)
