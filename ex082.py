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
numerospar = []
numerosimpar = []

for c in range(len(numeros)):
    if numeros[c] % 2 == 0:
        numerospar.append(numeros[c])
    else:
        numerosimpar.append(numeros[c])
print(f'A lista de numeros digitados é: {numeros}.\n'
      f'A lista de numeros \033[0;31mpares\033[m digitados é: {numerospar}.\n'
      f'A lista de numeros \033[0;31mimpares\033[m digitados é: {numerosimpar}.')
