class Cliente:
    def __init__(self):
        self.nome = ""
        self.filiado = False
        self.quantidade_item = 0

    def inserir_dados(self, nome, filiado, quantidade_item):
        self.nome = nome
        self.filiado = filiado
        self.quantidade_item = quantidade_item