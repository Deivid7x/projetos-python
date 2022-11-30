n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um numero: '))
n4 = int(input('Digite o ultimo numero: '))
numeros = n1, n2, n3, n4
print(f'Você digitou os valores {numeros}')
if 9 in numeros:
    print(f'O numero 9 apareceu {numeros.count(9)} vezes.')
else:
    print('O numero 9 não pareceu nenhuma vez.')
if 3 in numeros:
    print(f'O numero 3 apareceu na posição {numeros.index(3)+1}.')
else:
    print('O numero 3 não apareceu nenhuma vez.')
print('Os valores pares digitados foram: ', end='')
for c in numeros:
    if c % 2 == 0:
        print(f'{c} ', end='')
