sellers_name = input()
sellers_fixed_salary = float(input())
sellers_sold_value = (float(input())*15)/100

sellers_final_salary = sellers_fixed_salary + sellers_sold_value

print(f"TOTAL = R$ {sellers_final_salary:.2f}")
