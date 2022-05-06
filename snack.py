x, y = list(map(int, input().split()))

price_list = [0, 4, 4.5, 5, 2, 1.5]
value_of_pay = price_list[x] * y

print(f'Total: R$ {value_of_pay:.2f}')
