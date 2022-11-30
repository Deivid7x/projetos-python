dicio = {'nome': input('Nome do aluno: '), 'média': float(input('Média: '))}
if dicio['média'] >= 7:
    r = 'Aprovado'
else:
    r = 'Reprovado'
dicio['situação'] = r
print(f'Nome: {dicio["nome"]}\n'
      f'Média de {dicio["nome"]}: {dicio["média"]}\n'
      f'Situação é igual a {dicio["situação"]}')
