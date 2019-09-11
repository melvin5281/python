# # Strings are enclosed in quotations, either double or single.
# # This is to tell python to take that value literally.
# name = "Melvin Nyamongo"
# marks = '45+66+21+99+85'
# phone_number = "0706274552"
# print(type(phone_number))
# # print(name)
# # print(phone_number)
# # print(type(phone_number))
#
# # typecasting the above string to an integer
# phone_number = int(phone_number)
# print(phone_number)
# print(type(phone_number))
#
# # typecasting back to string
# phone_number = str(phone_number)
# print(type(phone_number))

# String operations

first_name = "melvin"
second_name = "Nyamongo"

# concatenating strings
# we use a plus operator to concat strings
full_name = first_name + second_name
print(full_name)

# to place an empty space in between the names we place a space string
full_name = first_name + " " + second_name
print(full_name)

print(first_name)
print(first_name.title())
print(first_name.upper())
print(first_name.lower())
print(full_name.split())
print(full_name.count("o"))

gender = "MMMFFFMFMMFMFMFMFMFFMFMFFFFFMMM"
print(gender.count("F"))
print(gender.swapcase())



