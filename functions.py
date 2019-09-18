# A function is a named reusable block of code, used to perform a related action

# a = 0
# b = 0
# a = a +2
# b = b +3

a = 0
b = []
c = {}
d = ()

# def is the key word python uses to create a new function
# 'add_two_numbers' is the name of our function
# a and b are called parameters of our function
# c is the return value

# def add_two_numbers(a,b):
#     c = a+b
#     return c

# def add_two_names(melvin,nyamongo):
#     c = melvin + nyamongo
#     return c
#
# first_name = input("Enter first name")
# second_name = input("Enter second name")
#
# result = add_two_names(first_name, second_name)
# print(result)
#

# def add_two_numbers(first,last):
#     full_name = first + last
#     return full_name
#
# res = add_two_names("Melvin","Nyamongo")
# print(res)
#

# student1 = [12,23,34,45,56]
# student2 = [22,23,34,45,56]
# student3 = [32,23,34,45,56]
# student4 = [42,23,34,45,56]
#
#
# total1 = student1[0] + student1[1] + student1[2] + student1[3] + student1[4]
# total2 = student2[0] + student2[1] + student2[2] + student2[3] + student2[4]
# total3 = student3[0] + student3[1] + student3[2] + student3[3] + student3[4]
# total4 = student4[0] + student4[1] + student4[2] + student4[3] + student4[4]
#
# average1 = total1/5
# average2 = total2/5
# average3 = total3/5
# average4 = total4/5
#
# def find_total(a,b,c,d,e):
#     complete_total = 12 + 23 + 34 +45 + 56
#     return complete_total
#
# res = find_total("a","b","c","d","e")
# print(res)
#
# def find_average(tot):
#     return tot/5
#
# res = find_average(total1/5)
# print(res)

# write a function called sum_digits that is given an integer num and returns the sum of the digits of num



def sum_digits(num):
    sum_of_digits = 0
    num = str(num)
    for i in num:
        sum_of_digits = sum_of_digits + int(i)
    return sum_of_digits


res = sum_digits(25)
print(res)

