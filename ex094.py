pessoas = []
while True:
    cadastro = {'nome': input('Nome: '),
                'sexo': input('Sexo: ').lower().strip(),
                'idade': int(input('Idade: '))}
    pessoas.append(cadastro.copy())
    del cadastro
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
print(pessoas)
print('=-'*20)
print(f'Foram cadastradas {len(pessoas)} pessoas.')

media = 0
for c in range(0, len(pessoas)):
    media = media + pessoas[c]['idade']
    if c == len(pessoas) - 1:
        media = media / len(pessoas)
print(f'A media de idade entre essas pessoas é: {media:.2f}')

print('As mulheres cadastradas foram: ', end='')
for c in range(0, len(pessoas)):
    if pessoas[c]['sexo'] == 'f':
        print(f'{pessoas[c]["nome"]} ', end='')

print('\nA lista de pessoas que estão acima da média de idade são:')
for c in range(0, len(pessoas)):
    if pessoas[c]['idade'] > media:
        print(f'{pessoas[c]}\n')
