# Synthax
""" 
for variable in iterable
  out
"""

"""
for i in 20:
    print(i)
    20 is not iterable
"""

for i in range(20):
  print(i)

course = {'PYTHON','JAVA','CSS','HTML'}
# for x in range(course):
   # print(f'{course[X]} is my favourite course')

# Dictionary
home = {
  "name": "James",
  "course": "python",
  "age": "18"
}
for k,v in home.items():
  print(k,v)

statement = "Coding with python is fun"
for y in statement:
  print(y)

list = ["Good","Good","Good","Good","Bad","Good","Good","Good","Good","Bad"]

for d in list:
  # break

  if d == "Bad":
    break
  print(d)

  # continue

  if d == "Bad":
    continue
  print(d)

for r in range(2, 52):
  if r%2 == 0:
   print(r)

# range can have(start, end, step)

for t in range(2, 11, 2):
  print(t)