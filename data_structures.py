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
#list_num_2 = [5, 7, 8]
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
# sports_list= [" "]
# user_input = input("which sport do you like: ")
# for each_sport in sports_list:    
#      new_list = sports_list.append(user_input)
#      print(new_list[each_sport])
#      new_input = input("enter your sport")

#------------assignment-----------------------
# sports_list = []
# user_input = input("Which sport do you like? ")
# sports_list.append(user_input)  # Add user input to the list once

# print("Updated sports list:")
# for each_sport in sports_list:
#     print(each_sport)  # Print each sport in the updated list
# user_input= input("enter another sport name : ")

# Initialize an empty list
sports_list = []


user_input = input("Which sport do you like? ")
sports_list.append(user_input)

print(sports_list)
# for each_sport in sports_list:
#     print(each_sport) 

user_input = input("Enter another sport (or type 'done' to finish): ")




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

#------------------------------------------FUNCTIONS---------------------------
#it is a block of reuseable code used to perform a simple related action

# def addition(num_1,num_2):
#     result = num_1 + num_2
#     #print(result)
#     return result

# add = addition(3,8) 
# print(f"the sum of the numbers is {add}")

# #----------------------------------------------

# def subtraction():
#     num_3 = int(input("enter first number: "))
#     num_4 = int(input("enter second number"))
#     answer = num_3  - num_4
#     print(answer)
#     return answer

# subtraction()

# #------------------------------------------------
# def division(num_5,num_6):
#     render= num_5 / num_6
#     return render
# divide = division(50,5)
# print(f"the division of the two numbers is {divide}")

# def user_inputs():
#     user_input_1 = int(input("enter the sales amount: "))
#     user_input_2 = float(input("enter the commission rate "))
#     return user_input_1 , user_input_2

# num_1 , num_2 = user_inputs()

# def sales_commission(num_1,num_2):
#     result = num_1 * num_2
#     return result
    
# commission = sales_commission(num_1,num_2) 
# print(f"your sale commission is : {commission}")


####-----------------------------------------------
#mkdir = is used to create a directory
#touch = used to create a file in a folder
#pandas and numpy is for data processing
#sea born is for data visualization

# pip --version
# pip --help
# pip freeze
# pip install
# pip download
# pip install pandas== 2.0.0 (used to install a specific version of a package)

##--------------------Virtual Environment----------------
#clone your repository
# create your virtual environment (python -m venv myenv)
#to check if the environment is activated (source myenv/Scripts/activate)
# you can install your packages
#             


# jupyter-notebook(to start the package)
#shutdown the kernel in the browser
# use ctrl-c in the terminal to interrupt
#use "deactivate" in terminal to close the environment

##---------loading and data processing--------------------------