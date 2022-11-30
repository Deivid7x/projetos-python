from math import pow, sqrt
co = float(input('Qual é o tamanho do cateto menor? '))
ca = float(input('Qual é o tamanho do cateto maior? '))
qco = pow(co, 2)
qca = pow(ca, 2)
hip = sqrt(qco+qca)
print(f'O comprimento da hipotenusa é: {hip:.2f}')
