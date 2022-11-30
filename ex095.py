jogadores = []
total = 0
gols = []
while True:
    print('-'*20)
    reg = {'nome': input('Nome do jogador: '),
           'partidas': int(input('Quantas partidas ele jogou? '))}
    for c in range(0, reg['partidas']):
        g = (int(input(f'Quantos gols na partida {c+1}? ')))
        gols.append(g)
        total = total + g
    reg['gols'] = gols.copy()
    gols.clear()
    reg['total'] = total
    jogadores.append(reg.copy())
    total = 0
    del reg

    r = input('Deseja continuar [S/N]?: ').lower().strip()
    if r == 'n':
        break
    while r != 's':
        print('Eu disse S ou N, animal!')
        r = input('Deseja continuar [S/N]?: ').lower().strip()
        if r == 'n':
            break
    if r == 'n':
        break
print('=-'*23)
print(f'COD   nome       gols         total\n'
      f'--------------------------------')
for c in range(0, len(jogadores)):
    print(f'{c: <6}{jogadores[c]["nome"]: <11}{str(jogadores[c]["gols"]):<13}'
          f'{jogadores[c]["total"]}')
print('-'*23)
dados = 0
while dados != 999:
    dados = int(input('Mostrar dados de qual jogador? [999 para encerrar]: '))
    if dados == 999:
        print('Volte sempre!')
        break
    print(f'Levantamento do jogador {jogadores[dados]["nome"]}:\n')
    for c in range(0, jogadores[dados]["partidas"]):
        print(f'No jogo {c+1} ele fez {jogadores[dados]["gols"][c]} gols.')
    print('-' * 23)
