pessoas = []
ind = []
maispesa = 0
maisleve = 0
while True:
    nome = input('Digite um nome: ')
    peso = float(input('Digite o peso: '))
    ind.append(nome)
    ind.append(peso)
    pessoas.append(ind[:])
    ind.clear()
    if peso >= maispesa:
        maispesa = peso
    if maisleve == 0:
        maisleve = peso
    elif peso <= maisleve:
        maisleve = peso
    print('Pessoa adicionada para a lista!')
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

print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {maispesa:.2f}. Peso de ', end='')
for c in range(0, len(pessoas)):
    if pessoas[c][1] == maispesa:
        print(f'{pessoas[c][0]} ', end='')

print(f'.\nO menor peso foi {maisleve:.2f}. Peso de ', end='')
for c in range(0, len(pessoas)):
    if pessoas[c][1] == maisleve:
        print(f'{pessoas[c][0]} ', end='')
print('.\n')
