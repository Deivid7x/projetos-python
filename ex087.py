numeros = []
linha = 0
coluna = 0
pares = terc = maior = 0
for c in range(0, 9):
    if c <= 2:
        numeros.append(int(input(f'Digite um valor para a posição[{linha},{coluna}]:')))
        coluna = coluna + 1
        if numeros[c] % 2 == 0:
            pares = pares + numeros[c]
        if coluna == 3:
            terc = terc + numeros[c]
    elif c <= 5:
        if linha == 0:
            coluna = 0
        linha = 1
        numeros.append(int(input(f'Digite um valor para a posição[{linha},{coluna}]:')))
        coluna = coluna + 1
        if numeros[c] % 2 == 0:
            pares = pares + numeros[c]
        if coluna == 3:
            terc = terc + numeros[c]
        if numeros[c] > maior:
            maior = numeros[c]
    elif c <= 9:
        if linha == 1:
            coluna = 0
        linha = 2
        numeros.append(int(input(f'Digite um valor para a posição[{linha},{coluna}]:')))
        coluna = coluna + 1
        if numeros[c] % 2 == 0:
            pares = pares + numeros[c]
        if coluna == 3:
            terc = terc + numeros[c]

print(f'[{numeros[0]: ^5}] [{numeros[1]: ^5}] [{numeros[2]: ^5}] \n'
      f'[{numeros[3]: ^5}] [{numeros[4]: ^5}] [{numeros[5]: ^5}] \n'
      f'[{numeros[6]: ^5}] [{numeros[7]: ^5}] [{numeros[8]: ^5}] \n')
print(f'A soma entre os numeros pares digitados é: {pares}\n'
      f'A soma entre os numeros da terceira coluna é: {terc}\n'
      f'O maior valor da segunda linha é {maior}')
