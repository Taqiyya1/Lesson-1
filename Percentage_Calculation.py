# Find the percentage he got?
print("Enter Marks Obtained in 4 subjects: ")
math = int(input("maths : "))
english = int(input("english : "))
science = int(input("science : "))
hindi = int(input("hindi : "))

sum = math+english+science+hindi
print("The sum of math, english, science, and hindi")

perc = (sum/400)*100

print(end="Percentage Mark = ")
print(perc)
