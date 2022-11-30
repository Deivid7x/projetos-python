from random import randint
print('Par ou impar!')
n = int(input('Digite um valor: '))
e = input('Par ou impar? [p/i]: ').lower().strip()
cont = 0
while True:
    c = randint(0, 10)
    s = (n + c) % 2
    if s == 0:
        if e == 'p':
            cont = cont + 1
            n = int(input(f' Você venceu. Escolhi {c}, e {c} + {n} é par.\n'
                          f'Digite outro valor:'))
            e = input('Par ou impar? [p/i]: ').lower().strip()
        elif e == 'i':
            print(f'Eu venci! Eu escolhi {c} e {c} + {n} é par.\n'
                  f'Você conseguiu {cont} vitorias antes de ser derrotado.')
            break
    else:
        if e == 'i':
            cont = cont + 1
            n = int(input(f' Você venceu. Escolhi {c}, e {c} + {n} é impar.\n'
                          f'Digite outro valor:'))
            e = input('Par ou impar? [p/i]: ').lower().strip()
        elif e == 'p':
            print(f'Eu venci! Eu escolhi {c} e {c} + {n} é impar.\n'
                  f'Você conseguiu {cont} vitorias antes de ser derrotado.')
            break
