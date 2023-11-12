from datetime import date


class Produto:
    def __init__(self):
        self.nome = ""
        self.preco = 0.0
        self.data_validade = date.today()

    def inserir_dados(self, nome, preco, data_validade):
        self.nome = nome
        self.preco = preco
        self.data_validade = data_validade