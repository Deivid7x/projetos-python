sal = float(input('Digite qual é o seu salario: '))
if sal > 1250:
    aum = (10/100)*sal
    print(f'Seu novo salario será de R${sal+aum:.2f} Reais.')
else:
    aum = (15/100)*sal
    print(f'Seu novo salario será de R${sal+aum:.2f} Reais')
