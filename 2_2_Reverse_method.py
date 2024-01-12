#reverse method
my_list1 = [11, 22, 33, 44, 55]
my_list1.reverse()

print("reverse method:")
for item in my_list1:
    print(item,end=" ")
print()

#slice method
my_list2 = [13, 32,53,74, 95]

print("reverse using slicing:")
for item in my_list2[::-1]:  
    print(item,end=" ")
