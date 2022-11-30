n = int(input('Digite um numero: '))
m = n - 1
r = 0
mult = 0
while m != 0:
    r = n * m
    if mult == 0:
        mult = r
    else:
        mult = mult * m
    m = m - 1
if mult == 0:
    print(f'{n}! = 1.')
else:
    print(f'{n}! = {mult}.')
