# Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant.
def total_calc(bill_amount,tip_perc):
    total = bill_amount*(1 + 0.01*tip_perc)
    total = round(total,2)
    print(f"Please pay ${total}")
    
total_calc(150,20)