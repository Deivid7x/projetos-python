nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split()
pri = lista[0]
print(f'O primeiro nome é: {pri}')
ultimo = lista[len(lista)-1]
print(f'O ultimo nome é: {ultimo}')
