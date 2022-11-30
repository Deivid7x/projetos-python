soma = 0
mvelho = 0
nmvelho = 0
contadordehomem = 0
contadordemulheres = 0
for c in range(1, 5):
    print(f'---- Pessoa {c} ----')
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo (m ou f): ').lower().strip()
    soma = soma + idade
    if sexo == 'm':
        contadordehomem = contadordehomem + 1
        if c == 1:
            mvelho = idade
            nmvelho = nome
        if idade > mvelho:
            mvelho = idade
            nmvelho = nome
    elif idade < 20:
        contadordemulheres = contadordemulheres + 1
print(f'A media da idade entre essas pessoas é: {soma/4:.2f} anos.')
if contadordehomem >= 1:
    print(f'O homem mais velho tem {mvelho} anos e se chama {nmvelho}.')
else:
    print('Não tem nenhum homem na lista.')
if contadordemulheres >= 1:
    if contadordemulheres == 1:
        print(f'Ao todo tem {contadordemulheres} mulher com menos de 20 anos.')
    else:
        print(f'Ao todo são {contadordemulheres} mulheres com menos de 20 anos.')
else:
    print('Não tem nenhuma mulher com menos de 20 anos na lista.')
