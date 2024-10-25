#import random

#--------------------FOR LOOP------------------------------
## generate sequence of numbs b/n  1 and 10
# for  each_number in range(0,10,2):
#     print("Each number:" , each_number)

## another way for for loop
# group_of_items= "Nathaniel"
# for each_item in group_of_items:
#     print(each_item)    



# class_reg = ["Nat", "Lyd" , "Yaf", "Jul"]    
# for each_item in class_reg:
#     print(each_item)

##ask the user to enter their name and print it out n number of times times
# user_names= input("Enter your name: ")
# number= int(input("Enter number of times: "))
# for each_name in range(number):
#     print("your name is: " , user_names)


##0041
# user_name= input("enter your name: ")
# number_times= int(input("enter number of times: "))
# if number_times<10:
#     for each_name in range(1,number_times+1):
#         print("your name is: ", user_name)
# else:
#     for each_item in range(1,4):
#         print("too high")       


#--------------------------------WHILE LOOP---------------------
#usual used in a case to test a statement of fact
# again= input("enter yes or no: ")
# while(again == "yes"):
#     print("hello")
#     #termination statement
#     again= input("do you want to continue: ")
# print("Goodbye")    

# total = 0
# while (total <= 10):
#     print("counter : ", total)
#     print("Hello world")
#     total =total + 1

# print("Goodbye")

# print("ATTENDANCE REGISTER")
# user_input=input("have you registered or not: ")
# while(user_input == "no"):
#     user_name= input("enter your name to register: ")
#     print("confirm name: " , user_name)


# 046
# user_input= int(input("enter a number: ")) 
# while(user_input <= 5):
#     print(user_input)
#     user_input=int(input("enter the next number"))

# print("the number you have entered is ", user_input)c

# action= "the boy is going to school"
# print(action.capitalize)


#------------random class-------------
# pick_item= random.choice(["red", "green", "blue"])
# print(pick_item)

# rand_num= random.randint(0,20)
# print(rand_num)

# num= random.random()
# print(num)


user_input= int(input("Enter a number between 10 and 20: "))
while((user_input<10) or (user_input>20)):
    if(user_input < 10):
        print("too low")
        #user_input=int(input("enter guess again: "))
    if(user_input > 20):
        print("too high ")    
        #user_input=int(input("enter guess again: "))
    user_input=int(input("enter guess again"))   
print
