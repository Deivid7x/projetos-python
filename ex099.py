from time import sleep


def linha():
    print('-='*30)


def maior(* num):
    m = 0
    for c in range(0, len(num)):
        if num[c] > m:
            m = num[c]
    linha()
    print('Analisando os numeros informados...')
    for c in range(0, len(num)):
        print(f'{num[c]} ', end='')
        sleep(0.5)
    print(f'Foram informados {len(num)} valores.\n'
          f'O maior valor informado foi {m}.')


maior(3, 5, 7)
maior(2, 8)
maior(9)
maior()
maior(6, 0, 32, 71, 12)
