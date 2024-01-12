def domainn(email):
  index = email.find("@")
  if index != -1:
    username = email[:index] 
    domain = email[index + 1:]  
    return username, domain
  else:
    print("Error")

email = input("Enter an email address: ")
username, domain = domainn(email)
if username and domain:
  print("Username:", username)
  print("Domain:", domain)
else:
  print("Invalid email address.")
