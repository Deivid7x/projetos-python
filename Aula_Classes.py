class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        # Definindo os ATRIBUTOS da minha classe.
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    # Definindo os MÉDOTOS
    def volume(self, botao):
        if botao == '+':
            print('Aumentando o volume')
        elif botao == '-':
            print('Diminuindo o volume')


# Atribuindo o objeto (ControleRemoto) a uma variavel (controle1)
controle1 = ControleRemoto('preto', '10cm', '3cm', '4cm')

# Chamando um ATRIBUTO do objeto criado com a classe
print(controle1.cor)

# Chamando um MÉTODO do objeto criado com a classe
controle1.volume('-')
