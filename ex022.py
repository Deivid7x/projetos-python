nome = input('Digite seu nome completo: ')
print(nome.upper())

print(nome.lower())
separo = nome.split()
junto = ''.join(separo)
nomese = len(junto)
print(f'Esse nome tem {nomese} caracteres, sem contar os espaços.')
cortado = separo[0]
pri = len(cortado)
print(f'O primeiro nome tem {pri} caracteres.')
