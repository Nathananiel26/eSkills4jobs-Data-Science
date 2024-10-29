# Data structure is a way of organizing data in a system
#----------List--------
#its a built in data structure used to store and manipulate  a collection of items
### creating an empty list

# empty_list = list()
# print(empty_list)

## creating another list  with 2,3,4
# list_nums = list([2, 3, 4,])
# print(list_nums)

## alternative
list_num_2 = [5, 7, 8]
# print(list_num_2)

##accessing the elements within a list
# print(list_num_2[1])
# print(list_num_2[2])

# for each_number in list_num_2:
#     print(each_number)

# for each_item in range(0, len(list_num_2)):
#     print(list_num_2[each_item])   
# print("----------------------------")
# print(len(list_num_2))


# ## list slicing
# house_items = ["car", 3, "dog", 2, "tv", "boys"]

# print(house_items[0:4])
# print(house_items[2: ])

# ##adding a new element to the list
# house_items.append("girls")
# print(house_items)

# print("---------------------")
# ##joining two list
# house_items.extend(list_num_2)
# print(house_items)

# ## inserting into a  particular index
# print("---------------------")
# house_items.insert(3, "blahhhh")
# print(house_items)

# ## returning the index of the list
# print("---------------------")
# print(house_items.index("boys"))

#example 71-------try your hands on it-------
# sports_list= ["football" , "volleyball"]
# user_input = input("which sport do you like: ")
# for each_sport in sports_list:    
#      new_list = sports_list.append(user_input)
#      print(new_list[each_sport])
#      new_input = input("enter your sport")

#------------assignment-----------------------
# sports_list = ["football", "volleyball"]
# user_input = input("Which sport do you like? ")
# sports_list.append(user_input)  # Add user input to the list once

# print("Updated sports list:")
# for each_sport in sports_list:
#     print(sports_list[each_sport])  # Print each sport in the updated list
#     user_input= input("enter name : ")



##-----------------------Dictionaries---------
# we use key to retrieve data from a dictionary
# it is similar to a database in programming construct
# two ways to create a dictionary is, "dict()"" or using "{}"
# my_dict= {"name" : "lillian",
#           "age" : 30,
#           "city" : "new york"}

# class_records = {
#                  1 : {"sam george", "class 6"},
#                  2 : {"lydia sam", "class 5"},
#                  3 : {"nat wood", "class 2"}
#                  }

# print(my_dict["age"])
# print(my_dict["city"])

# print(class_records[3])

#returning all the keys of a dictionary
# print(class_records.keys())

#returning all values of a dictionary
# print(class_records.values())

#inserting new record in a dictionary
# class_records[4] = {"sunday", "class 6"} 

# print(class_records)

# print("------------------------")
# var = class_records.keys()
# for each_item in class_records:
#     print(class_records[each_item])