# Write a program to satisfy the following conditions of the given range.

for x in range(10):
    if x % 20 == 0:
        print("twist")
        
    elif x % 15 == 0:
        pass
    
    elif x % 5 == 0:
        print("buzz")
        
    else:
        print(x)