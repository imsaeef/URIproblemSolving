value = int(input())

print(value)

for i in [100,50,20,10,5,2,1]:
    print(f'{value//i} nota(s) de R$ {i},00')
    value %= i
