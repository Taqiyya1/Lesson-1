# Write a program to understand how the value error exception works?

try: 
    number = int(input("Enter a Number: "))
    print("The number entered is", number)
    
except ValueError as ex:
    print("Exeption", ex)
    