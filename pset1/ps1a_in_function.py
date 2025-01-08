def part_a(yearly_salary, portion_saved, cost_of_dream_home):
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
	return months