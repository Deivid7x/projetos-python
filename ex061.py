t = int(input('digite o primeiro termo da sua progressão aritimetica: '))
r = int(input('Digite a razão da sua progressão aritimetica: '))
cont = 0
soma = 0
while cont != 10:
    cont = cont + 1
    soma = soma + r
    if soma == r:
        soma = t
    print(f'{soma}')
