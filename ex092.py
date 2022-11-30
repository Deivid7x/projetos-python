cad = {'nome': input('Digite o nome: '),
       'idade': 2022 - int(input('Digite o ano de nascimento: ')),
       'carteira': int(input('Digite sua carteira de trabalho: '))}
if cad['carteira'] != 0:
    cad['contr'] = int(input('Ano de contratação: '))
    cad['salario'] = float(input('Salário: '))
    cad['aposentadoria'] = (cad['contr'] - (2022 - cad['idade'])) + 35
    print(f'Nome: {cad["nome"]}\n'
          f'Idade: {cad["idade"]}\n'
          f'carteira: {cad["carteira"]}\n'
          f'Ano de contratação: {cad["contr"]}\n'
          f'Salário: {cad["salario"]:.2f}\n'
          f'Idade para se aposentar: {cad["aposentadoria"]}')
else:
    print(f'Nome: {cad["nome"]}\n'
          f'Idade: {cad["idade"]}\n'
          f'carteira: {cad["carteira"]}\n')
