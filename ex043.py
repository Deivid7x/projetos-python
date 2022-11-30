from math import pow
peso = float(input('Digite seu peso: '))
alt = float(input('Digite sua altura: '))
imc = peso / (pow(alt, 2))
if imc < 18.5:
    print('Voce está abaixo do peso.')
elif imc == 18.5 or imc > 18.5:
    if imc < 25:
        print('Você está no peso ideal.')
    elif imc == 25 or imc > 25:
        if imc < 30:
            print('Voce está com sobrepeso.')
        elif imc == 30 or imc > 30:
            if imc < 40 or imc == 40:
                print('Voce está obeso: ')
            else:
                print('Você está com obesidade mórbida.')
