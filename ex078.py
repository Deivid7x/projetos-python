n = list()
for c in range(5):
    n.append(int(input(f'Digite o valor para posição {c}: ')))
maior = max(n)
menor = min(n)

print('=-'*20)

print(f'O maior valor digitado foi {max(n)} na(s) posição(ções): ', end='')

for c in range(len(n)):
    if n[c] == maior:
        print(f'{c} ', end='')

print(f'\nO menor valor digitado foi {min(n)} na(s) posição(ções): ', end='')

for c in range(len(n)):
    if n[c] == menor:
        print(f'{c} ', end='')
