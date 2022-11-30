soma = 0
for c in range(6):
    n = int(input('Digite um numero inteiro: '))
    if n % 2 == 0:
        soma = soma + n
print(f'A soma entre todos os numeros pares que você digitou é: {soma}')
