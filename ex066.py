cont = soma = 0
n = int(input('Digite um numero, ou digite 999 para encerrar o programa: '))
while True:
    if n == 999:
        break
    cont = cont + 1
    soma = soma + n
    n = int(input('Digite outro numero, ou digite 999 para encerrar o programa.'))
if cont == 0:
    print('Você não digitou nenhum numero.\n'
          'Programa encerrado.')
else:
    print(f'Você digitou {cont} numeros.\n'
          f'A soma entre os numeros digitados é {soma}.\n'
          f'Programa encerrado.')
