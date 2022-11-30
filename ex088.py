from random import randint
from time import sleep
todos = []
jogo = []
num = 0
r = int(input('Quantos jogos você quer que eu crie? '))

for c in range(0, r):
    while len(jogo) < 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    print(f'Jogo {c + 1}: {jogo}')
    todos.append(jogo[:])
    jogo.clear()
    sleep(1)
