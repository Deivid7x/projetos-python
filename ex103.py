def ficha(n='', g=''):
    if n == '':
        n = '<Desconhecido>'
    if g == '':
        g = 0
    return f'O jogador {n} fez {g} gol(s) no campeonato.'


nome = input('Nome do jogador: ').strip().title()
gols = input('Numero de gols: ')
print(ficha(nome, gols))
