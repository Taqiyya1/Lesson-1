# Write a program to create a class Parrot and perform the following tasks:
# 1. Create a class variable species 
# 2. Create a __init__ method that has instance variables - name and age 
# 3. Create instances of class Parrot, passing arguments as well 
# 4. Print Class variable by accessing it 5. Print Instance variables as well

class Parrot:
    species = "bird"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))