portion_down_payment = 0.25
current_savings = 0
r = 0.04
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the portion of salary to be saved as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
monthly_salary = annual_salary/12
month = 0
# Part A ------------------------
while True:
	# print(current_savings, month)
	current_savings += current_savings*r/12 + monthly_salary*portion_saved
	month += 1
	if(current_savings >= total_cost*portion_down_payment):
		break
print("Number of month: ", month)
# Part B -------------------------
semi_annual_raise = float(input("Enter your semi annual raise in decimal: "))
current_savings = monthly_salary*portion_saved
month = 1
while True:
	# print(current_savings, month)
	if(month%6 == 0):
		monthly_salary *= 1 + semi_annual_raise
	current_savings += current_savings*r/12 + monthly_salary*portion_saved
	month += 1
	if(current_savings >= total_cost*portion_down_payment):
		break
print("Number of month: ", month)
#Part C ----------------------------
portion_down_payment = 0.25
current_savings = 0
r = 0.04
annual_salary = float(input("Enter your starting salary: "))
semi_annual_raise = 0.07
total_cost = 1000000
portion_down_payment = 0.25*total_cost
current_savings = 0
right = 10000
left = 0
# mid == portion_saved
step = 1
while True:
	# mid == portion_saved
	monthly_salary = annual_salary/12
	mid = (left + right)//2
	print("Initial current savings", current_savings)
	print(mid)
	month = 1
	while True:
		if(month%6 == 0):
			monthly_salary *= (1 + semi_annual_raise)
		current_savings += current_savings*r/12 + monthly_salary*(mid/10000)
		if month == 36:
			break
		else:
			month += 1
	print(current_savings)
	print("Portion down payment", portion_down_payment)	
	if (portion_down_payment - 100 < current_savings) & (current_savings < portion_down_payment + 100):
		break
	if (current_savings < portion_down_payment - 100):
		print("First case")
		left = mid
		current_savings = 0
	elif current_savings > portion_down_payment + 100:
		print("Second case")
		right = mid
		current_savings = 0
	step = step + 1
	if(step == 15):
		break
print("Best saving rate: %.2f" %(mid/10000))
print("Steps in bisection search:", step)

