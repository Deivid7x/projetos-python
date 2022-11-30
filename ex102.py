def fatorial(n, show=False):
    """

    :param n: Numero a ser calculado.
    :param show: Mostrar ou não a conta
    :return: O valor fatorial do numero 'n'.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f = f * c
    return f


print(fatorial(5, show=True))
