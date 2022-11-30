t = int(input('digite o primeiro termo da sua progressão aritimetica: '))
r = int(input('Digite a razão da sua progressão aritimetica: '))
result = 0
for c in range(10):
    result = result + r
    if result == r:
        result = t
    print(result)
