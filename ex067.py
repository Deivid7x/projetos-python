n = int(input('Tabuada!\n'
              'Digite um valor.'
              'Quando quiser parar digite um numero negativo.'))
while True:
    if n < 0:
        break
    print(f'{n} *  1 = {n * 1}')
    print(f'{n} *  2 = {n * 2}')
    print(f'{n} *  3 = {n * 3}')
    print(f'{n} *  4 = {n * 4}')
    print(f'{n} *  5 = {n * 5}')
    print(f'{n} *  6 = {n * 6}')
    print(f'{n} *  7 = {n * 7}')
    print(f'{n} *  8 = {n * 8}')
    print(f'{n} *  9 = {n * 9}')
    print(f'{n} * 10 = {n * 10}')

    n = int(input('Digite outro numero (ou numero negativo para encerrar.'))
print('Programa encerrado.')
