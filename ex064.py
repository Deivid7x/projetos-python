n = 0
soma = 0
cont = 0
while n != 999:
    n = int(input('Digite um numero [999 para encerrar]: '))
    soma = soma + n
    if n != 999:
        cont = cont + 1
if n == 999:
    if cont == 1:
        print(f'Programa encerrado.\n'
              f'Você digitou {cont} numero!'
              f'A soma entre os numeros que você digitou é: {soma - 999}.')
    elif cont == 0:
        print(f'Programa encerrado.\n'
              f'Você não digitou nenhum numero.'
              f'A soma entre os numeros que você digitou é: 0.')
    else:
        print(f'Programa encerrado.\n'
              f'Você digitou {cont} numeros!'
              f'A soma entre os numeros que você digitou é: {soma - 999}.')
