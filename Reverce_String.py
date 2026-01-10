# Write a program to reverse the string entered by the user.

string = input("Please enter you own string: ")

string2 = ('')

for i in string:
    string2 = i + string2

print("\nThe Original String = ", string)
print("\nThe Reversed String = ", string2)