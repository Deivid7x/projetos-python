from ex115.lib.interface import *
from ex115.lib.Arquivo import *
from time import sleep

arq = 'Dados dos clientes.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Programa encerrado. Até logo!')
        break
    else:
        print('\033[31mOpção invalida. Tente novamente.\033[m')
    sleep(2)
