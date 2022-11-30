maior18 = 0
mulher20 = 0
homens = 0

while True:
    idade = int(input('Idade: '))
    if idade > 18:
        maior18 = maior18 + 1
    sexo = input('Sexo [m/f]: ').lower().strip()
    if sexo == 'm':
        homens = homens + 1
    if sexo == "f":
        if idade < 20:
            mulher20 = mulher20 + 1
    continuar = input('Quer continuar [s/n]? ').lower().strip()
    if continuar == 'n':
        break
    while continuar != 's':
        continuar = input('Quer continuar [s/n]? ').lower().strip()
        if continuar == 'n':
            break
print(f'{maior18} pessoas tem mais de 18 anos.\n'
      f'{homens} homens foram cadastrados.\n'
      f'{mulher20} mulheres tem menos de 20 anos.')
