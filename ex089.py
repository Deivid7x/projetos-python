listona = []
alunos = []
notas = []
while True:
    alunos.append(input('Nome: '))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    alunos.append(notas[:])
    alunos.append((notas[0] + notas[1]) / 2)
    listona.append(alunos[:])
    alunos.clear()
    notas.clear()
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

print(f'No.   NOME        MÉDIA')
for c in range(0, len(listona)):
    print(f'{c:<6}{listona[c][0]:12}{listona[c][2]:.2f}')
while True:
    r = int(input('digite o numero do aluno que deseja saber a nota (ou 999 para encerrar): '))
    if r == 999:
        print('Programa encerrado.')
        break
    print(f'As notas de {listona[r][0]} são {listona[r][1]}')
