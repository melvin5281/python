# # # a whileloop repeats until a specified condition is false
# #
# # a = 10
# # # tha condition we are talking about is "a<10"
# # while a < 11:
# #     print(a)
# #     a = a+1
#
# # lets take a = 0
#
# a = 0
# while a < 11:
#     print("melvin "*a)
#     a = a+1

# a = 0
# while a < 101:
#     print(a)
#     a = a+2
#
# a = 1
# while a < 100:
#     print(a)
#     a = a+2

savedPin = "0000"
trials = 3

enteredPin = input("enter your pin")
trials = trials-1
while savedPin != enteredPin and trials>0:
    enteredPin = input("enter your pin")
    trials = trials-1
else:
    if trials<1 and enteredPin != savedPin:
        print("card blocked")
    else:
        print("successful login")