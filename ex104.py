def leiaint(n):
    if n == 'Digite um numero: ':
        n = input('Digite um numero: ')
        if n.isnumeric():
            return int(n)
        else:
            while not (type(n) == int):
                print('ERRO! Digite um numero inteiro.')
                n = input('Digite um numero: ')
                if n.isnumeric():
                    return int(n)


numero = leiaint('Digite um numero: ')
print(f'Voce digitou o numero {numero}.')
