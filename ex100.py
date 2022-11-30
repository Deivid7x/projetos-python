from time import sleep
from random import randint
numeros = []


def sorteia():
    for c in range(0, 5):
        numeros.append(randint(1, 10))
    print('Sorteando 5 valores: ', end='')
    for c in range(0, 5):
        print(f'{numeros[c]} ', end='')
        sleep(0.5)
    print('Pronto!')


def somapar():
    soma = 0
    for c in range(0, len(numeros)):
        if numeros[c] % 2 == 0:
            soma = soma + numeros[c]
    print(f'Somando os valores pares de {numeros}, temos: {soma}')


sorteia()
sleep(0.5)
somapar()
