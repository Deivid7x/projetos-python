cidade = input('Digite o nome de uma cidade: ')
dividido = cidade.split()
resultado = 'santo' in dividido[0]
print(f'Essa cidade começa com o nome santo? {resultado}')
