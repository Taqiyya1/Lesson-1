# Write a program to check whether the given number is greater than 15 or smaller than 15.

i = int(input("enter a number: "))
if (i < 15):
    print(i, "is smaller than 15")
    print("i'm in if Block")
else:
    print(i, "is greater than 15")
    print("i'm in else block")
print("i'm not in if and not in else")