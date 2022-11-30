n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print(f'Você foi reprovado por que sua media foi {media:.1f}.')
elif media == 7 or media > 7:
    print(f'Parabens, sua media foi {media:.1f}, você foi aprovado!')
elif media > 5:
    if media < 7:
        print(f'Ficou de recuperação. Sua media foi {media:.1f}.')
