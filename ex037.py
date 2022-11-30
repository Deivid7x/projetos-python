num = int(input('Digite um numero: '))
print('Escolha uma das bases decimais:\n'
      '1 para binario\n'
      '2 para octal\n'
      '3 para hexadecimal.')
escolha = int(input('Digite sua escolha: '))
if escolha == 1:
    print(f'{num} convertido para binario é {num:b}.')
elif escolha == 2:
    print(f'{num} convertido para octal é {num:o}.')
elif escolha == 3:
    print(f'{num} convertido para hexadecimal é {num:h}.')
else:
    print('Escolha uma das 3 opções.')
