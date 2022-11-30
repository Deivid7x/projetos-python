valor = int(input('Digite o valor que quer sacar: '))
ced = 50
totced = 0
while True:
    if valor >= ced:
        valor = valor - ced
        totced = totced + 1
    else:
        if totced > 0:
            print(f'{totced} cedulas de {ced}.')
        if valor < ced:
            ced = 20
            totced = 0
        if valor < ced:
            ced = 10
            totced = 0
        if valor < ced:
            ced = 1
            totced = 0
        if valor == 0:
            break
