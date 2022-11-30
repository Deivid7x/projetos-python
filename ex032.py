ano = int(input('Digite um ano: '))
ano4 = float(ano % 4)
if ano4+4 == 4:
    ano100 = float(ano % 100)
    if ano100+100 == 100:
        ano400 = float(ano % 400)
        if ano400+400 == 400:
            print(f'O ano {ano} é um ano bissexto.')
        else:
            print(f'O ano {ano} não é bissexto.')
    else:
        print(f'O ano {ano} é um ano bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
