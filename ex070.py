total = 0
mmil = 0
contmaisbarato = 0
mbarato = 0
nmaisbarato = 0
continuar = 0
nome = 0
while True:
    if continuar == 'n':
        break
    nome = input('Digite o nome do produto: ').strip()
    preco = float(input('Digite o preço do produto: '))
    continuar = input('Quer continuar [s/n]? ').lower().strip()
    total = total + preco
    if preco > 1000:
        mmil = mmil + 1
    contmaisbarato = contmaisbarato + 1
    if contmaisbarato == 1:
        nmaisbarato = nome
        mbarato = preco
    if preco < mbarato:
        nmaisbarato = nome
    if continuar == 'n':
        break
    while continuar != 's':
        continuar = input('Quer continuar [s/n]? ').lower().strip()
        if continuar == 'n':
            break
print(f'O total da compra foi: R${total:.2f} Reais.\n'
      f'{mmil} produtos custam mais de R$1000,00 Reais.\n'
      f'{nome} é produto mais barato da lista.')
