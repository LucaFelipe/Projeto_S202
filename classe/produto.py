from datetime import date
from classe.loja import Loja

class Produto:
    def __init__(self, database):
        self.database = database
    
    def create(self, nome, preco, data_validade, nome_loja):
        if Loja.verify(self, nome_loja) != []:
            try:
                query = "MATCH (l:Loja {nome: $nome_loja}) CREATE (p:Produto {nome: $nome, preco: $preco})-[:Pertence]->(l)"
                parameters = {"nome": nome, "preco":preco, "data_validade":data_validade, "nome_loja":nome_loja}
                self.database.execute_query(query, parameters)
                return "Produto criado!"
            except:
                return "Erro ao criar o produto"
        else:
            return "Loja não existe!"