#009
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
user_input1=int(input("enter first number: "))
user_input2= int(input("enter second number: "))
if user_input1 > user_input2:
    print("second number is ", user_input2 , "the first number is ", user_input1)
