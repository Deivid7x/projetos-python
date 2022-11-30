palavras = 'batata', 'pokemon', 'beyblade', 'naruto', 'yugioh', 'caderno'

for c in palavras:
    print(f'\nNa palavra {c} temos: ', end='')
    a = c.count('a')
    e = c.count('e')
    i = c.count('i')
    o = c.count('o')
    u = c.count('u')
    if a > 0:
        print('a ' * a, end='')
    if e > 0:
        print('e ' * e, end='')
    if i > 0:
        print('i ' * i, end='')
    if o > 0:
        print('o ' * o, end='')
    if u > 0:
        print('u ' * u, end='')
