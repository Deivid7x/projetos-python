maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Digite o peso da pessoa {c}: '))
    if c == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f' o maior peso é {maior:.2f} e o menor é {menor:.2f}')
