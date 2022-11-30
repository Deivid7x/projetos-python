def notas(*inp, sit=False):
    total = len(inp)
    maior = max(inp)
    menor = min(inp)
    media = 0
    for c in range(0, len(inp)):
        media += inp[c]
    media = media / len(inp)
    dicio = {'total': total, 'maior': maior, 'menor': menor, 'media': media}
    if sit:
        if media >= 7:
            dicio.update({'Situação': 'Boa'})
        elif media < 5:
            dicio.update({'Situação': 'Ruim'})
        else:
            dicio.update({'Situação': 'Mediana'})
    return dicio


resp = notas(2, 4, 3, 8, 7, sit=True)
print(resp)
