from functions import add_two_numbers
# we use while loops when we dont have a defined end of a loop
# for loop is a kind of loop that repeats until maximum is reached.

# for a in range(10,101):
#     print(a)

# fruits = ["Mango", "Apple", "Pears", "Bananas", "Avocado", "Pineapple", "Guava", "Strawberry"]
#
# for each in fruits:
#     each = each+" juice"
#     print(each)

# find the sum of numbers from 0-9
# sum = 0
# for each in range(10):
#     sum = each+ sum
#
# print(sum)

# name = "Melvin"
# for nam in range(101):
#     print(name)


# name = "Melvin"
# for each in range (101):
#
#     print(each,"name")



# for each in range(8,101,3):
#
#  print(each)

# for each in range(100,1,-2):
#     print(each)

# for each in range(1,21):
#     eachbyeach = each**2
#     print(each, "-----", eachbyeach)


first_number = input("Enter first number")
second_number = input("Enter second number")

result = add_two_numbers(first_number,second_number)
print(result)