import random
n = random.randint(1, 5)
ne = int(input('Pensei em um numero de 1 a 5, tente advinhar! '))
if ne == n:
    print(f'Muito bem! o numero que pensei foi exatamente {n}! Você venceu!')
else:
    print(f'Nada disso, o numero que pensei foi {n}! Eu venci!')
