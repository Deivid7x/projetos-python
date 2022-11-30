from math import radians, sin, cos, tan
ang = float(input('Digite um ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print(f'O seno de {ang} graus é: {sen:.2f}')
print(f'O coceno de {ang} graus é: {cos:.2f}')
print(f'A tangente de {ang} graus é: {tan:.2f}')