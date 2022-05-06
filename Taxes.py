salary = float(input())

if salary > 0 and salary <= 2000:
    print('Isento')
elif salary > 2000 and salary <= 3000:
    result = salary - 2000
    taxes = result * 0.08
    print(f'R$ {taxes:0.2f}')
elif salary > 3000 and salary < 4500:
    result = salary - 3000
    taxes = (result * 0.18) + (1000 * 0.08)
    print(f'R$ {taxes:0.2f}')
else:
    result = salary - 4500
    taxes = (result * 0.28) + (1500 * 0.18) + (1000 * 0.08)
    print(f'R$ {taxes:0.2f}')
