from ex115.lib.interface import *


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('ERRO ao criar arquivo.')
    else:
        print(f'Arquivo {nome} criado.')


def lerarquivo(nome):
    a = 0
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo.')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for pessoa in a:
            dado = pessoa.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('ERRO na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao escrever no arquivo.')
        else:
            print(f'Novo registro de {nome} criado!')
            a.close()
            