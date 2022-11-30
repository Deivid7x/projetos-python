vel = float(input(print('Qual a velocidade do carro? ')))
if vel > 80:
    print('Ultrapassou o limite de velociadade!')
    print(f'A multa vai custar R${(vel-80)*7:.2f} Reais.')
