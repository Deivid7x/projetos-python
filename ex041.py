ano = int(input('Digite o seu ano de nascimento: '))
idade = 2022 - ano
if idade == 9 or idade < 9:
    print('Sua categoria é Mirim.')
elif idade > 9:
    if idade < 14 or idade == 14:
        print('Sua categoria é infantil.')
    else:
        if idade < 19 or idade == 19:
            print('Sua categoria é junior.')
        else:
            if idade < 20 or idade == 20:
                print('Sua categoria é senior.')
            else:
                print('Sua categoria é master.')
