n = int(input('Digite um numero inteiro: '))
div = 0
for c in range(1, n + 1):
    if n % c == 0:
        div = div + 1
if div == 2:
    print(f'O numero {n} é um numero primo.')
else:
    print(f'O numero {n} não é primo.')
