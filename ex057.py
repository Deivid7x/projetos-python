sexo = input('Digite seu sexo [m/f]: ').lower().strip()
while sexo not in 'mf':
    sexo = input('Digite novamente seu sexo, apenas "m" ou "f".')
r = 0
if sexo == 'm' :
    r = 'Masculino'
if sexo == 'f':
    r = 'Feminino'
print(f'Entendi, então você é do sexo {r}.')
