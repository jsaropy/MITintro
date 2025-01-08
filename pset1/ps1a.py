## 6.100A PSet 1: Part A
## Name: Shvan Jaro
## Time Spent: 3.5 hours
## Collaborators: None

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################

yearly_salary = float(input("Yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Cost of Dream Home: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

portion_down_payment = 0.25
down_payment_cost = cost_of_dream_home * portion_down_payment
amount_saved = float(0)
r = 0.05
monthly_salary= yearly_salary / 12
monthly_saved = monthly_salary * portion_saved
months = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

while amount_saved <= down_payment_cost:
    amount_saved += amount_saved * (r/12)
    amount_saved += monthly_saved
    months += 1

print(months)