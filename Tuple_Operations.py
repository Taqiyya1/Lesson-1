# Write a program to perform the following operations: 
# 1. Create a tuple with different datatypes 
# 2. Create another tuple of integers 
# 3. Create a new tuple by adding 9 to the previous tuple 
# 4. Count the occurrences of an element in the tuple 
# 5. Perform slicing on the tuple

tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

tuplex = (4, 6, 2, 8, 3, 1)
print(tuplex)

tuplex = tuplex + (9,)
print(tuplex)

tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))
