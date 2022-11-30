valor = float(input('Digite o valor da casa: '))
sala = float(input('Digite o seu salário: '))
tempo = float(input('Digite em quantos anos pretende pagar: '))
prest = valor / (tempo * 12)
porc = (30/100) * sala
if prest > porc:
    print('Infelizmente não podemos lhe conceder um emprestimo.')
elif porc > prest:
    print(f'O valor das parcelas mensais será de: R${prest:.2f} Reais.')
