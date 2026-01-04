# Write to check a number is divisible by another number

print("Enter a Number (Numerator): ")
numN = int(input())

print("Enter a number (Denominator): ")
numD = int(input())

if numN%numD==0:
    print("\n" +str(numN)+ " is divisible by " +str(numD))
else:
    print("\n" +str(numN)+ " is not divisible by " +str(numD))