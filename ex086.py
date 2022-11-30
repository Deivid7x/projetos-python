numeros = []
linha = 0
coluna = 0
for c in range(0, 9):
    if c <= 2:
        numeros.append(int(input(f'Digite um valor para a posição[{linha},{coluna}]:')))
        coluna = coluna + 1
    elif c <= 5:
        if linha == 0:
            coluna = 0
        linha = 1
        numeros.append(int(input(f'Digite um valor para a posição[{linha},{coluna}]:')))
        coluna = coluna + 1
    elif c <= 9:
        if linha == 1:
            coluna = 0
        linha = 2
        numeros.append(int(input(f'Digite um valor para a posição[{linha},{coluna}]:')))
        coluna = coluna + 1

print(f'[{numeros[0]: ^5}] [{numeros[1]: ^5}] [{numeros[2]: ^5}] \n'
      f'[{numeros[3]: ^5}] [{numeros[4]: ^5}] [{numeros[5]: ^5}] \n'
      f'[{numeros[6]: ^5}] [{numeros[7]: ^5}] [{numeros[8]: ^5}] \n')
