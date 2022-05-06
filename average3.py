a, b, c, d = map(float, input().split())

avg = (a*2 + b*3 + c*4 + d*1) / 10

print(f'Media: {avg:0.1f}')

if avg >= 7.0:
    print("Aluno aprovado.")
elif avg < 5.0:
    print("Aluno reprovado.")
elif avg >= 5.0 and avg < 7.0:
    print("Aluno em exame.")
    e = float(input())
    print(f'Nota do exame: {e:0.1f}')
    avg2 = (e + avg) / 2
    if avg2 >= 5.0:
        print("Aluno aprovado.")
        print(f'Media final: {avg2:0.1f}')
    else:
        print("Aluno reprovado.")
        print(f'Media final: {avg2:0.1f}')
