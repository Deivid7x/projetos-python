numeros = []
while True:
    n = int(input('Digite um numero: '))
    numeros.append(n)
    print('Numero adicionado para a lista!')
    r = input('Deseja continuar [S/N]?: ').lower().strip()
    if r == 'n':
        break
    while r != 's':
        print('Eu disse S ou N, animal!')
        r = input('Deseja continuar [S/N]?: ').lower().strip()
        if r == 'n':
            break
    if r == 'n':
        break
numeros.sort(reverse=True)
print(f'Foram digitados {len(numeros)} numeros.\n'
      f'Os numeros digitados em ordem decrescente são: {numeros}')
if 5 in numeros:
    print('O numero 5 foi digitado!')
else:
    print('O numero 5 não foi digitado :( ')
