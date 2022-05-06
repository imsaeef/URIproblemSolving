x = int(input())

odd_list = []

while True:
    if x%2 == 1:
        print(x)
        odd_list.append(x)
        if len(odd_list) == 6:
            break
    x += 1