p=n=e=o= 0

for i in range(5):
    x = int(input())
    if x>0:
        p += 1
    elif x<0:
        n += 1
    if x % 2 == 0:
        e += 1
    else:
        o += 1
print(f'''{e} valor(es) par(es)
{o} valor(es) impar(es)
{p} valor(es) positivo(s)
{n} valor(es) negativo(s)''')