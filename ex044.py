valor = float(input('Digite o valor do produto: '))
cond = int(input('Digite a condição do pagamento:\n'
                 'à vista dinheiro/cheque, digite: 1\n'
                 'à vista no cartão, digite: 2\n'
                 'em até 2x no cartão, digite: 3\n'
                 'Se for pagar em 3x ou mais no cartão, digite: 4\n'))
if cond == 1:
    print(f'Com 10% de desconto, você pagará: {valor-((10/100)*valor):.2f} Reais.')
elif cond == 2:
    print(f'Com 5% de desconto, você pagará: {valor-((5/100)*valor):.2f} Reais.')
elif cond == 3:
    print(f'Você não terá desconto, então pagará: {valor:.2f} Reais.')
elif cond == 4:
    print(f'O novo valor do produto será: {valor+((20/100)*valor):.2f} Reais.')
