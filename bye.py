# Write a program using nested while loop. If the value is divided by two, then it will run an infinite loop of the bye.

valid = False
while not valid:
    try:
        n = int(input("Enter a number: "))
        while n%2==0:
            print("bye")
            valid = True
    except ValueError:
        print("Invalid")