from random import randint
quantos = int(input('Quantos numeros quer jogar? '))

jogo = []
ultimosSorteios = [4, 15, 22, 53, 56, 60, 3, 5, 32, 56, 57, 59]
jaJogados = []
for c in range(0, quantos):
    for n in range(0, 6):
        numero = randint(1, 60)
        while numero in jogo or numero in ultimosSorteios or numero in jaJogados:
            numero = randint(1, 60)
        jogo.append(numero)
        jaJogados.append(numero)
        if len(jogo) == 6:
            for cada in range(0, 6):
                print(f'{jogo[cada]} ', end='')
                if cada == 5:
                    print('')
    jogo.clear()
