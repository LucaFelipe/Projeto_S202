from datetime import date
from classe.cliente import Cliente
from classe.loja import Loja
from classe.produto import Produto
from database.database import Database
import datetime


class Main:
    def __init__(self):
        self.db = Database()
        self.do_crud()
        
    def do_crud(self):
        aux = True
        while(aux):
            print("Bem vindo ao gerenciador de lojas!")
            print("OPCOES DISPONIVEIS:")
            print("1 - Criar loja")
            print("2 - Criar produto")
            print("3 - Criar cliente")
            print("Outra opção - Sair")
            opcao = input()
            match opcao:
                case "1": 
                    nome = input("Nome da loja: ")
                    endereco = input("Endereco da loja: ")
                    lucro_mensal = int(input("Lucro mensal: "))
                    l = Loja(self.db)
                    print(l.create(nome, endereco, lucro_mensal))
                case "2":
                    nome = input("Nome do produto: ")
                    preco = input("Preco: ")
                    data_validade = datetime.datetime.now()
                    nome_loja = input("Nome da loja correspondente: ")
                    p = Produto(self.db)
                    print(p.create(nome, preco, data_validade, nome_loja))
                case _:
                    aux = False

main_instance = Main()