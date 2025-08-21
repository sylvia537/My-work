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

number = int(input("please enter a number: "))
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

i = 0
for i in reversed(range(i, number)):
  print(i)
else:
  print(f'{number} numbers printedddd')

i = 0
while i in reversed(range(i, number)):
  print(i)
  i += 1
else:
  print(f'{number}numbers printed')