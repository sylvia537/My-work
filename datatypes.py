 # commenting
'''

primitive
Strings
integers
Boolean
none'''

"""

Data collections
List
Tuple
Dictionary
Set"""
# string :Anything within a quote either single or double
name ='Sylvia'
print(type(name))
age ='16'
print(type(age))
School ="G skills"
print(type(School))
testing ='''
we are 
learning 
python
'''
print(type(testing))
txt = "we are learning python"
# String properties
print(len(txt))
print(txt[0])
# Slicing
print(txt[0:2])
print(txt[0:6])
print(txt[:7])
print(txt[2:])
print(txt[:-1])
print(txt[-1:])
print(txt[-7:])
# name = input("please enter your name: ")
# print(name)

# name = input("please enter your name: ")
# course = input("please enter your course: ")
# email = input("please enter your email: ")
# print(name , "is studying" , course , "his email is" , email)

# # string formating
# print(f'{name} is studying {course} and his email is {email}')

# # String methods
# Course = input("please enter your course: ")
# print(course.upper())
# print(Course.lower())

#
# print(f'name: {name}')
# print(f'course: {course}')
# print(f'age: {age}')
# print(f'email: {email}')
# print(f'phone_no: {phone_no}')

# print(F'name: {name}\nage: {age}\ncourse: {course}\nemail: {email}\nphone_no: {phone_no}')

# integer
score = 56
print(type(score))
price = 5.2
print(type(price))
Is_student = True
print(type(Is_student))
is_working = False
print(type(is_working))
friends = []
print(type(friends))
friends = ['John','Peter','Paul','Moses']
print(friends)
print(friends[0])
print(f'{friends[0]} is my friend')
print(friends[0:2])
print(friends[-1:])
friends.append('James')
print(friends)
friends.append('Mark')
print(friends)
friends.insert(2,'Mathew')
print(friends)
friends.pop()
print(friends)

# dictionary
student = {}
print(type(student))
student = {
    "name":'John',
    "age": 20,
    "course": 'python',
    "email": 'John@gmail.com',
}
print(student)
print(student.keys())
print(student.values())
print(student.items())
student.update({"phone": '07073928972'})
print(student)

#tuple
family = ()
print(type(family))
family = ('John','James','Peter')
print(family)

# Assignment
my_list = [10, 20, 30, 40, 50]
print(my_list)
print(my_list[2])
print(list(my_list))
my_list = []
if not my_list:
     print("The list is empty")
else:
     print("The list is not empty")

my_list = [10, 20, 30, 40, 50]
my_list[1] = 200
print(my_list)

my_list.append(600)
print(my_list)
my_list.insert(2,300)
print(my_list)
my_list.pop()
print(my_list)
my_list.pop(0)
print(my_list)
my_list = [10, 20, 30, 40, 50]
total_sum = sum(my_list)
print(total_sum)

if my_list:
     average = total_sum / len(my_list)
else:
     average = 0
print(f'sum of the list: {total_sum}')
print(f'Average of the list: {average}')

# Set
course = {'HTML','CSS','PYTHON','JS','HTML'}
print(type(course))
print(course)
course.add("JAVA")
print(course)