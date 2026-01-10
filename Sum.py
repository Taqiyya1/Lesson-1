# Write a program to calculate the sum of whole numbers.

n = int(input("Enter the number whose sum you want to find: "))
sum = 0

for i in range(1, n+1):
    sum = sum+1
    print("\nSum =", sum)