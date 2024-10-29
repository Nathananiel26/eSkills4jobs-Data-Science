##009
# Write a program that will ask for a number of days and then will show how
# many hours, minutes and seconds are in that number of Days

# user_days= int(input("enter number of days: "))
# num_hours= user_days* 24
# print("the number of hours in ", user_days, "is " , num_hours)
# num_mins= num_hours * 60
# print("the number of minutes is ", num_mins)
# num_secs= num_mins * 60
# print("the number of secs is ", num_secs)

#010
# Task the user to enter a number over 100 and then enter a number under
# 10 and tell them how many times the smaller number goes into the larger
# number in a user-friendly format

# user_input1= int(input("enter a number above 100: "))
# user_input2= int(input("enter a number below 10"))
# opr= user_input1 / user_input2 
# print(user_input2, " enters into " , user_input1, " by " , opr, "times")

# 012
# Ask for two numbers. If the first one is larger than the second, display the second number
# first and then the first number, otherwise show the first number first and then the second.
# user_input1=int(input("enter first number: "))
# user_input2= int(input("enter second number: "))
# if user_input1 > user_input2:
#     print("second number is ", user_input2 , "the first number is ", user_input1)
# else:
#     print("first number ",user_input1, "second number ", user_input2)    

#------------------------for loops-----------------------------------
##35
# user_name= "Nathaniel"
# for each_name in user_name:
#     print(each_name)

# user_name= input("please enter your name: ")
# for each_name in range (1,4) :
#     print("Your name is :", user_name)

##36
# user_name= input("please enter your name: ")
# number= int(input("enter number to print: "))
# for each_name in range(number):
#     print("your name is : ", user_name, " and you chose: ", number)

##37
# user_name= input("enter your name: ")
# for each_text in user_name:
#     print(each_text)

##38
# user_name = input("enter your name: ")
# user_number = int(input("enter a number: "))
# for i in range(user_number):
#     for each_letter in user_name:
#         print(each_letter)
#     print("--------------")
 
##39
#user_input = int(input("enter a number between 1 to 10: "))
# if(1 < user_input < 13 ):
#     print(f"times table for {user_input}") 
#     for i in range (1,13):
#         print(f"{user_input} * {i} = {user_input * i}")        
# else:
#     print("out of range")        

##40
# user_input = int(input("enter a number below 50: "))
# if(1 <= user_input <= 50):
#     for i in range (user_input,0, -1):
#         print(i)
# else :
#     print("ont of range")

##41
# user_input = input("enter your name: ")
# user_number = int(input("enter a a number: "))
# if (user_number < 10):
#     for each_name in range(user_number):
#         print("my name is : ", user_input)
# else: 
#     print("number out of range")

##42
# Set a variable called total to 0. Ask the user to enter five numbers and after each input ask
# them if they want that number included. If they do, then add the number to the total. If they
# do not want it included, don’t add it to the total. After they have entered all five numbers,
# display the total.
total = 0
user_input = int(input("enter five numbers : "))
for each_input in range(1,6):
    print("the number you entered is ",user_input)
    next_number = int(input('pls enter next num : '))

