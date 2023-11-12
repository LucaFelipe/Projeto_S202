class Cliente:
    def __init__(self):
        self.nome = ""
        self.quantidade_item = 0

    def inserir_dados(self, nome, quantidade_item):
        self.nome = nome
        self.quantidade_item = quantidade_item