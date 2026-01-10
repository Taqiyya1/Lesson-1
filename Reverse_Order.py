# Write a program to print the numbers in reverse order beginning from the number entered by the user.

n = int(input("Enter the value of n: "))

print("numbers from {0} to {1} are: ".format(n,1))

for i in range(n,0,-1):
    print(i)