from classe.produto import Produto
from classe.cliente import Cliente
from classe.loja import Loja
from database.database import Database

def exibir_menu():
    print("==== MENU ====")
    print("1 - Criar produto")
    print("2 - Criar cliente")
    print("3 - Criar loja")
    print("4 - Ler produto")
    print("5 - Ler cliente")
    print("6 - Ler loja")
    print("7 - Atualizar cliente")
    print("8 - Atualizar produto")
    print("9 - Atualizar loja")
    print("10 - Deletar cliente")
    print("11 - Deletar produto")
    print("12 - Deletar loja")
    print("0 - Sair")
    print("================")

def criar_produto(produto):
    nome = input("Informe o nome do produto: ")
    preco = float(input("Informe o preço do produto: "))
    data_validade = input("Informe a data de validade do produto: ")
    nome_loja = input("Informe o nome da loja do produto: ")
    resultado = produto.create(nome, preco, data_validade, nome_loja)
    print(resultado)

def criar_cliente(cliente):
    nome = input("Informe o nome do cliente: ")
    quantidade = int(input("Informe a quantidade do produto comprada pelo cliente: "))
    item = input("Informe o nome do produto comprado pelo cliente: ")
    resultado = cliente.create(nome, quantidade, item)
    print(resultado)

def criar_loja(loja):
    nome = input("Informe o nome da loja: ")
    endereco = input("Informe o endereço da loja: ")
    lucro_mensal = float(input("Informe o lucro mensal da loja: "))
    numero_funcionarios = int(input("Informe o número de funcionários da loja: "))
    resultado = loja.create(nome, endereco, lucro_mensal, numero_funcionarios)
    print(resultado)

def ler_produto(produto):
    nome = input("Informe o nome do produto para leitura: ")
    resultado = produto.read(nome)
    print(resultado)

def ler_cliente(cliente):
    nome = input("Informe o nome do cliente para leitura: ")
    resultado = cliente.read(nome)
    print(resultado)

def ler_loja(loja):
    nome = input("Informe o nome da loja para leitura: ")
    resultado = loja.read(nome)
    print(resultado)

def atualizar_cliente(cliente):
    nome = input("Informe o nome do cliente para atualizar: ")
    novo_nome = input("Informe o novo nome do cliente: ")
    resultado = cliente.update(nome, novo_nome)
    print(resultado)

def atualizar_produto(produto):
    nome = input("Informe o nome do produto para atualizar: ")
    novo_nome = input("Informe o novo nome do produto: ")
    novo_preco = float(input("Informe o novo preço do produto: "))
    nova_data_validade = input("Informe a nova data de validade do produto: ")
    resultado = produto.update(nome, novo_nome, novo_preco, nova_data_validade)
    print(resultado)

def atualizar_loja(loja):
    nome = input("Informe o nome da loja para atualizar: ")
    novo_nome = input("Informe o novo nome da loja: ")
    novo_endereco = input("Informe o novo endereço da loja: ")
    novo_lucro_mensal = float(input("Informe o novo lucro mensal da loja: "))
    novo_numero_funcionarios = int(input("Informe o novo número de funcionários da loja: "))
    resultado = loja.update(nome, novo_nome, novo_endereco, novo_lucro_mensal, novo_numero_funcionarios)
    print(resultado)

def deletar_cliente(cliente):
    nome = input("Informe o nome do cliente para deleção: ")
    resultado = cliente.delete(nome)
    print(resultado)

def deletar_produto(produto):
    nome = input("Informe o nome do produto para deleção: ")
    resultado = produto.delete(nome)
    print(resultado)

def deletar_loja(loja):
    nome = input("Informe o nome da loja para deleção: ")
    resultado = loja.delete(nome)
    print(resultado)

# Inicialização do banco de dados
database = Database()
produto = Produto(database)
cliente = Cliente(database)
loja = Loja(database)

# Loop do menu
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Saindo do programa...")
        database.close()  # Fechar a conexão com o banco de dados antes de sair
        break
    elif opcao == "1":
        criar_produto(produto)
    elif opcao == "2":
        criar_cliente(cliente)
    elif opcao == "3":
        criar_loja(loja)
    elif opcao == "4":
        ler_produto(produto)
    elif opcao == "5":
        ler_cliente(cliente)
    elif opcao == "6":
        ler_loja(loja)
    elif opcao == "7":
        atualizar_cliente(cliente)
    elif opcao == "8":
        atualizar_produto(produto)
    elif opcao == "9":
        atualizar_loja(loja)
    elif opcao == "10":
        deletar_cliente(cliente)
    elif opcao == "11":
        deletar_produto(produto)
    elif opcao == "12":
        deletar_loja(loja)
    else:
        print("Opção inválida. Por favor, escolha novamente.")
