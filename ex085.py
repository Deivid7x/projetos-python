todos = []
par = []
impar = []

for c in range(0, 6):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
par.sort()
impar.sort()

todos.append(par)
todos.append(impar)

print(f'Os valores pares digitados foram: {par}.\n'
      f'Os valores impares digitados foram: {impar}')
