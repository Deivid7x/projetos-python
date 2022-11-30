n1 = input('Digite um numero: ')
n2 = input('Digite outro numero: ')
n3 = input('Digite um ultimo numero: ')
if n1 > n2:
    if n1 > n3:
        print(f'{n1} é o maior numero.')
        if n2 > n3:
            print(f'{n3} é o menor numero.')
        else:
            print(f'{n2} é o menor numero')
    else:
        print(f'{n3} é o maior numero')
        print(f'{n2} é o menor numero')
else:
    if n2 > n3:
        print(f'{n2} é o maior numero.')
        if n1 > n3:
            print(f'{n3} é o menor numero.')
        else:
            print(f'{n1} é o menor numero.')
    else:
        print(f'{n3} é o maior numero.')
        print(f'{n1} é o menor numero.')
        