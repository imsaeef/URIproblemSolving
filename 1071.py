x = int(input())
y = int(input())

sum = 0

for i in range(x-1,y,-1):
    if i%2 == 1:
        sum += i

print(sum)

#done............