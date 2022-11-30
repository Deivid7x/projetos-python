import random
jog = str(input('Vamos jogar jokenpo.\n'
                'Digite: pedra, papel ou tesoura. ')).lower()
pedra = 1
papel = 2
tesoura = 3
lista = [pedra, papel, tesoura]
comp = random.choice(lista)

if jog == 'pedra':
    if comp == pedra:
        print('Empatamos! Também escolhi Pedra.')
    elif comp == papel:
        print('Haha, venci! Escolhi Papel!')
    else:
        print('Você venceu dessa vez. Escolhi Tesoura.')
elif jog == 'papel':
    if comp == pedra:
        print('Você venceu dessa vez. Escolhi Pedra.')
    elif comp == papel:
        print('Empatamos! Também escolhi Papel.')
    else:
        print('Haha, venci! Escolhi Tesoura!')
elif jog == 'tesoura':
    if comp == pedra:
        print('Haha, venci! Escolhi Pedra!')
    elif comp == papel:
        print('Você venceu dessa vez. Escolhi Papel.')
    else:
        print('Empatamos! Também escolhi Tesoura.')
else:
    print('Digite uma das opções válidas.')
