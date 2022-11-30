import random
n = random.randint(1, 10)
n1 = float(input('Pensei em um numero inteiro de 1 a 10, tente advinhar: '))
if n1 >= 1:
    if n1 > 10:
        print('Perdeu. Eu disse um numero de 1 a 10.')
    else:
        if n == n1:
            print(f'Você venceu! o numero que pensei foi {n}! Parabens!')
        else:
            print(f'Errrrrrou! O numero que pensei foi {n}.')
else:
    print('Perdeu. Eu disse um numero de 1 a 10.')
