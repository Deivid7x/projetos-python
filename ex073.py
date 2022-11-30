times = ('são paulo', 'bahia', 'palmeiras', 'santos', 'fluminense', 'bota fogo', 'flamengo',
         'nankatsu', 'akatsuki', 'corvinal')
print(f'Os cinco primeiros são: {times[0: 5]}')
print(f'Os quatro ultimos são: {times[6:]}')
print(f'Os times em ordem alfabetica: {sorted(times)}')
print(f'Nankatsu está na posição {times.index("nankatsu")+1}')
