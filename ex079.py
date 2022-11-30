numeros = list()
while True:
    n = int(input('Digite um numero: '))
    if n in numeros:
        print('Valor duplicado. O numero não será adicionado.')
    else:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    cont = input('Deseja continuar? [S/N]').lower().strip()
    if cont == 'n':
        break
    while cont != 's':
        print('Eu disse S ou N, animal!')
        cont = input('Deseja continuar? [S/N]').lower().strip()
        if cont == 'n':
            break
numeros.sort()
print(f'Você digitou os valores {numeros}')
