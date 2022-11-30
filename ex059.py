n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
comando = 0
while comando != 5:
    comando = int(input('Digite:\n'
                        '[1] para somar\n'
                        '[2] para multiplicar\n'
                        '[3] para saber o maior valor\n'
                        '[4] para digitar novos numeros\n'
                        '[5] para encerrar o programa\n'
                        ''))
    if comando == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}!')
    if comando == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}!')
    if comando == 3:
        if n1 > n2:
            print(f'O numero {n1} é maior que o numero {n2}!')
        elif n2 > n1:
            print(f'O numero {n2} é maior que o numero {n1}!')
        elif n1 == n2:
            print('Os numeros são iguais!')
    if comando == 4:
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero: '))
    if comando == 5:
        print('Programa encerrado!')
