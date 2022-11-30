r1 = float(input('Digite o tamanho da primeira reta: '))
r2 = float(input('Digite o tamanho da segunda reta: '))
r3 = float(input('Digite o tamanho da terceira reta: '))
if (r1 + r2) > r3:
    if (r1 + r3) > r2:
        if (r2 + r3) > r1:
            print('Essas medidas podem formar um triangulo!')
        else:
            print('Essas medidas não podem formar um triangulo!')
    else:
        print('Essas medidas não podem formar um triangulo!')
else:
    print('Essas medidas não podem formar um triangulo!')
