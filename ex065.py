r = 's'
soma = 0
maior = 0
menor = 0
cont = 0
while r == 's':
    n = int(input('Digite um numero: '))
    soma = soma + n
    cont = cont + 1
    if cont == 1:
        maior = n
        menor = n
    elif cont > 1:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer continuar? digite s = sim // n = não. ')).lower().strip()
print(f'A media entre os valores digitados é: {soma / cont}.\n'
      f'O maior valor digitado foi {maior}.\n'
      f'O menor valor digitado foi {menor}.')
