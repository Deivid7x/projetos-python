from time import sleep

registro = {'nome': input('Digite o nome: ')}
partidas = int(input(f'Quantas partidas {registro["nome"]} jogou? '))

listag = []
totalgols = 0

for c in range(0, partidas):
    gols = int(input(f'Quantos gols ele marcou na partida {c+1}? '))
    listag.append(gols)
    totalgols = totalgols + gols

registro['gols'] = listag.copy()
registro['total'] = totalgols

print('Calculando...')
sleep(2)

print(f'Nome: {registro["nome"]}\n'
      f'Gols em cada partida: {registro["gols"]}\n'
      f'Ele marcou no total: {registro["total"]} Gols.')
print('=-'*20)

print('Preparando dados detalhados...')
sleep(3)

print(f'O jogador {registro["nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'   => Na partida {c+1}, ele fez {registro["gols"][c]}')
print(f'Foi um total de {registro["total"]} gols.\n')

sleep(2)

print('Programa encerrado.')
