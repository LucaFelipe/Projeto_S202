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
            print("1 - Ver opcoes para loja")
            print("2 - Ver opcoes para produto")
            print("3 - Ver opcoes para cliente")
            print("Outra opção - Sair")
            opcao = input()
            match opcao:
                case "1": 
                    self.op_loja()
                case "2":
                    self.op_produto()
                case "3":
                    self.op_clientes()
                case _:
                    exit()
                    
    def op_loja(self):
        aux = True
        l = Loja(self.db)
        while(aux):
            print("\nOPCOES PARA LOJAS:")
            print("1 - Criar loja")
            print("2 - Ver loja pelo nome")
            print("3 - Atualizar loja")
            print("4 - Excluir loja pelo nome")
            print("5 - Voltar")
            print("Outra opcao - Sair")
            opcao = input()
            match opcao:
                case "1":
                    nome = input("Nome da loja: ")
                    endereco = input("Endereco da loja: ")
                    lucro_mensal = int(input("Lucro mensal: "))
                    num_func = int(input("Numero de funcionarios: "))
                    print(l.create(nome, endereco, lucro_mensal, num_func))
                case "2":
                    nome = input("Nome da loja: ")
                    print(l.read(nome))
                case "3":
                    nome = input("Nome atual da loja: ")
                    novo_nome = input("Nome novo da loja: ")
                    novo_lucro = input("Novo lucro mensal: ")
                    novo_end = input("Novo endereço: ")
                    novo_nfunc = input("Novo numero de funcionarios: ")
                    print(l.update(nome, novo_nome, novo_end, novo_lucro, novo_nfunc))
                case "4":
                    nome = input("Nome da loja: ")
                    print(l.delete(nome))
                case "5":
                    self.do_crud()
                case _:
                    exit()
    
    def op_produto(self):
        aux = True
        p = Produto(self.db)
        while(aux):
            print("\nOPCOES PARA PRODUTO:")
            print("1 - Criar produto")
            print("2 - Ver produto pelo nome")
            print("3 - Atualizar produto")
            print("4 - Excluir produto pelo nome")
            print("5 - Voltar")
            print("Outra opcao - Sair")
            opcao = input()
            match opcao:
                case "1":
                    nome = input("Nome do produto: ")
                    preco = input("Preco: ")
                    data_validade = datetime.datetime.now()
                    data_validade = data_validade.strftime("%x")
                    nome_loja = input("Nome da loja correspondente: ")
                    print(p.create(nome, preco, data_validade, nome_loja))
                case "2":
                    nome = input("Nome do produto: ")
                    print(p.read(nome))
                case "3":
                    nome = input("Nome atual do produto: ")
                    novo_nome = input("Novo nome: ")
                    novo_preco = input("Novo preço: ")
                    print(p.update(nome, novo_nome, novo_preco))
                case "4":
                    nome = input("Nome do produto: ")
                    print(p.delete(nome))
                case "5":
                    self.do_crud()
                case _:
                    exit()
    
    def op_clientes(self):
        aux = True
        c = Cliente(self.db)
        while(aux):
            print("\nOPCOES PARA CLIENTES:")
            print("1 - Criar cliente")
            print("2 - Ver cliente pelo nome")
            print("3 - Atualizar cliente")
            print("4 - Excluir cliente pelo nome")
            print("5 - Voltar")
            print("Outra opcao - Sair")
            opcao = input()
            match opcao:
                case "1":
                    nome = input("Nome do cliente: ")
                    item = input("Nome do item adquirido: ")
                    quantidade = input("Quantidade de itens: ")
                    print(c.create(nome, quantidade, item))
                case "2":
                    nome = input("Nome do cliente: ")
                    print(c.read(nome))
                case "3":
                    nome = input("Nome atual do cliente: ")
                    novo_nome = input("Novo nome do cliente: ")
                    print(c.update(nome, novo_nome))
                case "4":
                    nome = input("Nome do cliente: ")
                    print(c.delete(nome))
                case "5":
                    self.do_crud()
                case _:
                    exit()
                    
            
main_instance = Main()