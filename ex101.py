def voto(ano):
    idade = 2022 - ano
    if idade >= 70 or idade == 16 or idade == 17:
        return f'Com {idade} anos, o voto é OPCIONAL.'
    elif idade < 16:
        return f'Com {idade} anos, você NÃO vota.'
    else:
        return f'Com {idade} anos, VOTO OBRIGATORIO.'


a = int(input('Digite o ano de nascimento: '))
print(voto(a))
