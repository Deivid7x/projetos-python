n = input('Digite algo: ')
print('Esse algo é do tipo: {}'.format(type(n)))
print('Esse algo é um numero? {}'.format(n.isnumeric()))
print('Esse algo é uma letra ou palavra? {}'.format(n.isalpha()))
