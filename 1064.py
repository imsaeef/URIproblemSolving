num = 0
sum = 0.0
for i in range(1, 7):
    x = float(input())
    if x > 0:
        sum = sum + x
        num += 1

print('{} valores positivos'.format(num))
print('%0.1f' % (sum / num))
