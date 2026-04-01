#Write a program to create a set and perform the following operations on that set- 
# 1. Create a set with integer elements 
# 2. Create a set with mixed data type elements 
# 3. Create another set with elements - 1, 2, 3, 4, 3, 2 
# 4. Create a set from a list with elements - [1, 2, 3, 2] 
# 5. Print the set after removing the first element from this set - [0, 1, 3, 4, 5]

my_set = {1, 2, 3}
print(my_set)

my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

my_set = set([1, 2, 3, 2])
print(my_set, "\n")

num_set = set([0, 1, 3, 4, 5])
print("Original set:")
print(num_set)
num_set.pop()
print("after removing the first elementfrom the said set:")
print(num_set,"\n")