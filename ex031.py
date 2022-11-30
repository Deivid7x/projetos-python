dis = float(input('Qual a distancia da sua viagem em km? '))
if dis <= 200:
    print(f'Voce pagará R${dis*0.5:.2f} Reais por essa viagem.')
else:
    print(f'Você pagará R${dis*0.45:.2f} Reais por essa viagem.')
