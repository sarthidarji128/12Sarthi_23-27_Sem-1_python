def get_user_info(*args, **kwargs):
    name = args[0]
    email = args[1]
    age = kwargs.get("age")
    return name, email, age
name = input("Enter your name: ")
email = input("Enter your email: ")
age = input("Enter your age: ")
name, email, age = get_user_info(name, email, age=age)
print("Name:", name)
print("Email:", email)
print("Age:", age)
