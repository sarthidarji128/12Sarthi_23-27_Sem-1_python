def get_distinct_elements_set(input_list):
    distinct_set = set(input_list)  
    return list(distinct_set) 

def get_distinct_elements_loop(input_list):
  distinct_list = []  
  seen = set()  
  for item in input_list:
    if item not in seen:
      distinct_list.append(item)
      seen.add(item)
  return distinct_list

def get_distinct_elements_user_input():
  input_str = input("Enter a list of numbers separated by spaces: ")
  input_list = []
  for num_str in input_str.split():
    input_list.append(int(num_str)) 

  distinct_list = get_distinct_elements_set(input_list) 
  print("Distinct elements:", distinct_list)


get_distinct_elements_user_input()
