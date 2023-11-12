from datetime import date
from Projeto_S202.classe.cliente import Cliente
from Projeto_S202.classe.loja import Loja
from Projeto_S202.classe.produto import Produto


class Main:
    def __init__(self):
        self.run()

    def run(self):
        minha_loja = Loja()
        meu_produto = Produto()
        meu_cliente = Cliente()
        
if __name__ == "__main__":
    Main()