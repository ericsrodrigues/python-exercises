name = input("")
fixed_salary = float(format((float(input(""))), '.2f'))
sales = float(format((float(input(""))), '.2f'))
final_salary = sales * 0.15 + fixed_salary

print (f"TOTAL = R$ {format(final_salary, '.2f')}")