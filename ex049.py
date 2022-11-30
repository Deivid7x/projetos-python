n = int(input('Digite um numero: '))
cont = 0
for c in range(1, 11):
    cont = cont + 1
    r = n * cont
    print(f'{n} x {cont} = {r} ')
