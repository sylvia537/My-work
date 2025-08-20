# Unary operator
a = 5
a += a
print(a)
x = 5
y = 2
print(f'x + y ={x + y}')
print(f'x - y ={x - y}')
print(f'x / y ={x / y}')
print(f'x // y ={x // y}')
print(f'x % y ={x % y}')
print(f'x * y ={x * y}')
print(f'x ** y ={x ** y}')

# comparison opertor
"""
== equal to
> Greater than
< Less that
>= Greater than or equal to
<= Less than or equal to
not"""

#age = int(input('please enter your age: '))
#print(type(age))
#print(age == 20)
#print(f'{age} = 20 is {age == 20}')
#print(f'{age} > 20 is {age > 20}')
#print(f'{age} < 20 is {age < 20}')
#print(f'{age} >= 20 is {age >= 20}')
#print(f'{age} <= 20 is {age <= 20}')

# Logical operator
#name = input('please enter your name: ')
# print(age == 20 and name == 'John')
# print(f'age = 20 and name = John is {age == 20 and name == 'John'}')
# print(f'age = 18 and name = John is {age == 18 and name == 'John'}')
# print(f'age = 20 and name = James is {age == 20 and name == 'James'}')
# print(f'age = 18 and name = James is {age == 18 and name == 'James'}')

# or logic
# print(f'age = 20 or name = John is {age == 20 or name == 'John'}')
# print(f'age = 18 or name = John is {age == 18 or name == 'John'}')
# print(f'age = 20 or name = James is {age == 20 or name == 'James'}')
# print(f'age = 18 or name = James is {age == 18 or name == 'James'}')

#if statement: 
""" if the condition is True:
      True
"""
x = 10
if x > 5:
    print('working')
if x < 5:
    print('Good')
else:
    print('not working')

friend = input("What is your name: ").title()
if friend == "John":
    print(f'{friend}, Good to see you today')
elif friend == "James":
    print(f'{friend}, How is studies')
elif friend == "Peter":
    print(f'{friend}, How is work')
else: 
    print(f'{friend}, please have we met before')