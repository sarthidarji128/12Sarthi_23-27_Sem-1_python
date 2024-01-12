a = [1, 2, 3]
extended = a + [4, 5]
print("Extended list using + operator:", extended)

a.append(6)
a.append(7)
print("Extended list using append():", a)

a.extend([8, 9])
print("Extended list using extend():", a)
