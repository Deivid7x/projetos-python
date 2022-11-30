frase = input('Digite uma frase: ').lower()
A = frase.count('a')
print(f'A letra "a" aparece {A} vezes nessa frase.')
pri = frase.find('a')+1
print(f'A letra "a" aparece pela primeira vez na posição {pri}')
ult = frase.rfind('a')+1
print(f'A letra "a" aparece pela ultima vez na posição {ult}')
