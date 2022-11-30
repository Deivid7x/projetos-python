import random
n = random.randint(1, 10)
ne = int(input('Pensei em um numero de 1 a 10, tente advinhar! '))
cont = 1
while ne != n:
    ne = int(input('Errrrrrrrooou, tente novamente: '))
    cont = cont + 1
print(f'Muito bem! pensei no numero {n}. Você precisou de {cont} tentativas para acertar.')
