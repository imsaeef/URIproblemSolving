salary = float(input())

if salary <= 400:
    percentage = 15
elif salary <= 800:
    percentage = 12
elif salary <= 1200:
    percentage = 10
elif salary <= 2000:
    percentage = 7
else:
    percentage = 4

me = (salary*percentage)/100
ns = me+salary

print(f'''Novo salario: {ns:0.2f}
Reajuste ganho: {me:0.2f}
Em percentual: {percentage} %''')
