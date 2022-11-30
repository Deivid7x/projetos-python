ano = int(input('Digite seu ano de nascimento: '))
idade = 2022 - ano
falta = 18 - idade
passou = idade - 18
if idade < 18:
    print(f'Ainda não está na hora de se alistar. faltam {falta} Anos.')
elif idade == 18:
    print('Já esta na hora de se alistar, boa sorte.')
elif idade > 18:
    print(f'Já passou da hora de se alistar, você devia ter se alistado {passou} Anos atrás.')
    