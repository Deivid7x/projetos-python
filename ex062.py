t = int(input('digite o primeiro termo da sua progressão aritimetica: '))
r = int(input('Digite a razão da sua progressão aritimetica: '))
cont = 0
soma = 0
amais = 0
novocont = 0
while cont != 10:
    cont = cont + 1
    soma = soma + r
    if soma == r:
        soma = t
    print(f'{soma}')
amais = int(input('Voce quer mais quantos termos? '))
if amais != 0:
    while novocont != amais:
        novocont = novocont + 1
        soma = soma + r
        print(f'{soma}')
        if novocont == amais:
            amais = int(input('Voce quer mais quantos termos? '))
            if amais != 0:
                novocont = 0
            elif amais == 0:
                novocont = 0
                print('Programa encerrado.')
elif amais == 0:
    print('Programa encerrado.')
