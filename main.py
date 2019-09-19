import bisect

annual_salary = float(input("Enter your annual salary: "))
total_cost = 1000000
semi_annual_raise = .07
total_months = 36
current_month = 0
current_savings = 0
down_payment_total = total_cost * .25
portion_saved_list = [i for i in range(0, 10)]

while current_month <= total_months:

    current_month += 1
    if current_month % 6 == 0:
        salary_raise = annual_salary * semi_annual_raise   
        annual_salary += salary_raise


    for i in portion_saved_list:
        res = i
        print(i)

    roi = (current_savings * .04 / 12)
    monthly_salary = annual_salary / 12

# else:
#    print("DOWN PAYMENT NEEDED ", down_payment_total)
#    print("CURRENT SAVINGS ", current_savings)
#    print("number of months needed to save: ", total_months)
