# Write a program to display 1 to 10 numbers in reverse order and skip the number 5.

var = 10              #initialize
while var > 0:        #iterate loop
    var = var - 1     
    if var == 5:      #Condition 1
        continue      #Continue Statement
        #Display result
    print("\nCurrent variable value:", var)
print("\nGood bye!")