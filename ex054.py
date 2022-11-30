cont = 0
for c in range(7):
    ano = int(input('Digite seu ano de nascimento: '))
    idade = 2022 - ano
    if idade < 18:
        cont = cont + 1
maior = 7 - cont
print(f'{cont} dessas pessoas ainda não atingiram a maioridade, e {maior} já são adultos.')
