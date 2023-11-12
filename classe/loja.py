class Loja:
    def __init__(self):
        self.nome = ""
        self.endereco = ""
        self.lucro_mensal = 0.0

    def inserir_dados(self, nome, endereco, lucro_mensal):
        self.nome = nome
        self.endereco = endereco
        self.lucro_mensal = lucro_mensal