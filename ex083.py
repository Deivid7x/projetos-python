exp = input('Digite uma expressão que tenha parenteses: ')
aberto = exp.count('(')
fechado = exp.count(')')
if aberto == fechado:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
