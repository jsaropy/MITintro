yearly_salary = float(input("Yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Cost of Dream Home: "))

portion_down_payment = 0.25

down_payment_cost = cost_of_dream_home * portion_down_payment

amount_saved = float(0)

r = 0.05

monthly_save = (yearly_salary * portion_saved) / 12
annual_rate_month = amount_saved * (r/12)

month = 0

while amount_saved < down_payment_cost:
    amount_saved += monthly_save

    if month > 0:
        amount_saved += amount_saved * (r/12)

    month += 1

print(int(month))