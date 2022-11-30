import random
nome1 = input('Me diga o nome do seu aluno: ')
nome2 = input('Me diga o nome de outro aluno: ')
nome3 = input('Me diga o nome de outro aluno: ')
nome4 = input('Me diga o nome de outro aluno: ')
lista = [nome1, nome2, nome3, nome4]
res = random.choice(lista)
print(f'O aluno escolhido foi {res}!')


