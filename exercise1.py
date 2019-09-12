taskList = [23, "Jane", ["Lesson 23", 560, {"currency": "KES"}], 987, (76, "John")]

# 1. Determine the type of variable in taskList using an inbuilt function
print(type(taskList))
a = type(taskList)
print(a)
# 2. Print KES
print(taskList[2][2]["currency"])
# or
first = taskList[2]
print(first)
second = first[2]
print(second)
# 3. Print 560
print(taskList[2][1])
# 4. Use a function to determine the length of taskList
print(len(taskList))
# 5. Rotate 987 to 789 using indexing only
x = taskList[3]
# change x from int to str
x = str(x)
# to rotate using indexing we use ::-1
x = x[::-1]
print(x)

# 6. Change the name "John" to "Jane"
# n/a
# John is in a tuple, you cant change values in a tuple


