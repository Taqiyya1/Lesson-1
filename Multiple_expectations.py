# Write a program to check how the exceptions and finally statement works

try: 
    num1, num2 = eval(input("Entertwo numbers, seperated by a comma: "))
    result = num1 / num2print("Result is", result)

except ZeroDivisionError:
    print("Division by zero is error!!")
    
except SyntaxError:
    print("Comma is missing. Enter numbers seperated by comma like this: 1, 2...")
    
except:
    print("wrong input")
    
else:
    print("No excpectations")
    
finally:
    print("This will execute no matter what")
    