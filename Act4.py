#Write a program to change the datatype of given variables?

name = "Taqiyya"
age = 14
is_student = True
weight = 55.5

print("Name :", name)
print("Data type of Name is", type(name))

print("Age :", age)
print("Data type of Age is", type(age))

print("Is_student :", is_student)
print("Data type of Is_student is", type(is_student))

print("weight :", weight)
print("Data type of weight is", type(weight))

print("\n After Type Casting...")
age = str(age)
print(age)
print("Data type of age is", type(age))
weight = int(weight)
print(weight)
print("Data type of weight is", type(weight))
