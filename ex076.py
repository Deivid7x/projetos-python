lista = 'pc', 5000, 'teclado', 100, 'mouse', 100, 'monitor', 1000
print('-'*31)
print(f'\033[0;31m{"LISTA DE COMPRAS":^31}\033[m',)
print('-'*31)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<20}', end='')
        c = c + 1
        print(f'R${lista[c]:>9.2f}')
