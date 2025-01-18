## 6.100A PSet 1: Part C
## Name: Shvan Jaro
## Time Spent: 
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit"))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
house_cost = 800000
down_payment = house_cost * 0.25
months = 36
steps = 0
low = 0
high = 1
r = (high + low) / 2.0
amount_saved = initial_deposit * (1+r/12)**months

max_possible_amount = initial_deposit * (1+1.0/12)**months

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
while amount_saved > down_payment + 100 or amount_saved < down_payment - 100:
    if max_possible_amount < down_payment - 100:
        r = None
        break

    if initial_deposit * (1+r/12)**months > down_payment:
        high = r
    else:
        low = r
    r = (high + low) / 2.0
    amount_saved = initial_deposit * (1+r/12)**months
    steps += 1

print(steps)
print(r)