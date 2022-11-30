n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero inteiro: '))
if n1 > n2:
    print(f'{n1} é o maior numero')
elif n2 > n1:
    print(f'{n2} é o maior numero')
elif n1 == n2:
    print('Os numeros são iguais.')
