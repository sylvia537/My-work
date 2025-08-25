# Synthax
# """ 
# for variable in iterable
#   out
# """

# """
# for i in 20:
#     print(i)
#     20 is not iterable
# """

# for i in range(20):
#   print(i)

# course = {'PYTHON','JAVA','CSS','HTML'}
# for x in range(course):
   # print(f'{course[X]} is my favourite course')

# Dictionary
# home = {
#   "name": "James",
#   "course": "python",
#   "age": "18"
# }
# for k,v in home.items():
#   print(k,v)

# statement = "Coding with python is fun"
# for y in statement:
#   print(y)

# list = ["Good","Good","Good","Good","Bad","Good","Good","Good","Good","Bad"]

# for d in list:
#   # break

#   if d == "Bad":
#     break
#   print(d)

#   # continue

#   if d == "Bad":
#     continue
#   print(d)

# for r in range(2, 52):
#   if r%2 == 0:
#    print(r)

# # range can have(start, end, step)

# for t in range(2, 11, 2):
#   print(t)


# # finite while loop
# """ 
# while condition:
# output
# increment/decreament
#  """
# print("-------------------------while---------------------------")
# i = 0
# while i <= 20:
#   print(i)
#   i += 1


#   # Assignment
#   # Print values from 1 to 100 when the value is 3 u print wuse, when the value is 5 u print Abuja otherwise print the number.

# for u in range(1, 101):  
#   print(u)
# u = 3
# if u > 3:
#    print('wuse')
# elif u < 5:
#   print('Abuja')
# else:
#   print(u)

# for i in range(1, 101):
#  if i%3 == 0:
#    print('wuse')
#  if i%5 == 0:
#    print('Abuja')
#  else:
#    print(i)

# infinite while loop


# """
#       syntax
#       While true:
#       code
#       if <condition>: 
#         break
#       code
      
# """
#  while True:
#    print(2)

# #\ user_number = int(input("please enter a number: "))
#  while int(user_number) < 20:
#   print("your guessed number is less than 20") 
# user_number = int(input("please enter a number: "))
# print("you guess is correct")

# QUESTION = """
#   Which of the following is a programming language
#   A: Microsoft Word
#   B: Python
#   C: HTML
#   D: Power BI
# """
# print(QUESTION)
# while True:
#    choose_correct_option = input("please choose a,b,c or d or choose q to quit: ").lower()
#    if choose_correct_option == "a":
#     print(f'{choose_correct_option} is not the correct answer because it is used for creating and formatting documents')
#     break
#    elif choose_correct_option == "b":
#     print(f'{choose_correct_option} is the correct option because pythons main purpose is to create codes')
#     break
#    elif choose_correct_option == "c":
#     print(f'{choose_correct_option} is not the correct answer because it is used for webpage creation')
#     break
#    elif choose_correct_option == "d":
#     print(f'{choose_correct_option} is not the correct answer because it is used for programming language')
#     break
#    elif  choose_correct_option == "q": 
#      print("You selected {choose_correct_option}! to quit the menu")
#      break
#    else:
#      print("You selected an invalid option")
#      break

# number = int(input("please enter a number: "))
# else with loop
# number = int(input("please enter a number: "))
# for i in range(number):
#   print(i)
# else:
#   print(f'{number} numbers printed')

# i = 0
# while i in range(i, number):
#   print(i)
#   i += 1
# else:
#   print(f'{number} numbers printed')

# i = 0
# for i in reversed(range(i, number)):
#   print(i)
# else:
#   print(f'{number} numbers printedddd')

# i = 0
# while i in reversed(range(i, number)):
#   print(i)
#   i += 1
# else:
#   print(f'{number}numbers printed')


# assignment
# Build a basic calculator that will add, subtract, multiply and divide.

# QUESTION = """
# IF 1 + 1 = 2; THEN 5 + 10 =?
# A: 6
# B: 10
# C: 19
# D: 15
# """
# print(QUESTION)
# while True:
#  choose_correct_option = input("please choose a,b,c or d or choose q to quit: ").lower()
#  if choose_correct_option == "a":
#    print(f'{choose_correct_option} is not the correct answer because 5 + 10 =/ 6')
#    break
#  elif choose_correct_option == "b":
#    print(f'{choose_correct_option} is not the correct answer because 5 + 10 =/ 10')
#    break
#  elif choose_correct_option == "c":
#    print(f'{choose_correct_option} is not the correct answer because 5 + 10 =/ 19')
#    break
#  elif choose_correct_option == "d":
#    print(f'{choose_correct_option} is not the correct answer because 5 + 10 = 15')
#    break
#  elif choose_correct_option == "q":
#    print("You selected {choose_correct_option}! to quit the menu")
#    break
#  else:
#    print("You selected an invalid option")
#    break
 
# work_1 = int(input("please enter the first number: "))
# work_2 = int(input("please enter the second number: "))
# work_3 = int(input("please enter the third number: "))
# print('Addition of {} + {} + {} ='.format(work_1,work_2,work_3))
# print(work_1 + work_2 + work_3)
# print('Subtraction of {} - {} - {} ='.format(work_1,work_2,work_3))
# print(work_1 - work_2 - work_3)
# print('Multiplication of {} * {} * {} ='.format(work_1,work_2,work_3))
# print(work_1 * work_2 * work_3)
# print('Division of {} / {} / {} ='.format(work_1,work_2,work_3))
# print(work_1 / work_2 / work_3)
# t = 1-3-2
# print(t)

# for i in range(1, 21):
#    if i%2 != 0:
#       print(i)

# u = 2
# while u <= 20:
#    if u%u == 0 and u%1 ==0:
#       print(u)
#       u += 3

list = [1,2,3,4,5]
new_list = []
for i in list:
    new_list.append(i * 3)
print(new_list)

friends_list = ['john', 'james', 'peter']
new_list = []
for i in friends_list:
    new_list.append(i.title())
    print(new_list)

# list comprehension
"""
variable = [operation loop condition]
"""
list = [1,2,3,4,5]
result = [i * 3 for i in list]
print(result)

friends_list = ['john', 'james', 'peter']
new_list = [i.title() for i in friends_list]
print(new_list)

list = []
new_list = [i for i in range(1,51) if i%2 == 0]
print(new_list)

a = ['a',1,'b',5,7,'cat',10]
new_list = [i for i in a if type(i) == str]
new_list2 = [i for i in a if type(i) == int]
new_list3 = [new_list + new_list2]
print(new_list)
print(new_list2)
print(new_list3)

# b = ['a','b','cat']
# c = [1,5,7,10]
# d = b + c
# print(d)

# Dictionary comprehension
percentage_increase = 5/100
product_list = {
    "phone":300000,
    "ipad":500000,
    "laptop":600000,
    "Buildings":900000,
    "homes":700000,
}
price_increase = {p:v + (v * percentage_increase) for p,v in product_list.items()}
print(price_increase)

percentage_decrease = 5/100
grocery_list = {
    "15 pens": 25000,
    "books": 67000,
    "calculator": 50000,
}
price = sum(grocery_list.values())
price_decrease = {p:v - (v * percentage_decrease) for p,v in grocery_list.items() if v > 60000}
print(price_decrease)