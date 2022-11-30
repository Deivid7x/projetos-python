from time import sleep


def linha():
    print('-'*30)


def contador(inicio, fim, passo):
    if inicio < fim:
        if passo < 0:
            passo = passo * -1
        if passo == 0:
            passo = 1
        linha()
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}: ')
        fim = fim + 1
        for cont in range(inicio, fim, passo):
            sleep(0.3)
            print(f'{inicio} ', end='')
            inicio = inicio + passo
        sleep(0.3)
        print('Fim!')
    elif inicio > fim:
        if passo < 0:
            passo = passo * -1
        if passo == 0:
            passo = 1
        linha()
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}: ')
        passo = passo * - 1
        fim = fim - 1
        for cont in range(inicio, fim, passo):
            sleep(0.3)
            print(f'{inicio} ', end='')
            inicio = inicio + passo
        sleep(0.3)
        print('Fim!')


contador(1, 10, 1)
contador(10, 1, 2)

a = int(input('inicio: '))
b = int(input('Fim: '))
c = int(input('Intervalo: '))

contador(a, b, c)
