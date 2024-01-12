def count(string):
  u = 0
  l = 0
  for char in string:
    if char.isupper():
      u += 1
    elif char.islower():
      l += 1

  return u, l

string_test = 'Today is My Best Day'
u, l = count(string_test)

print("Number of uppercase letters:", u)
print("Number of lowercase letters:", l)
