from classe.produto import Produto


class Cliente:
    def __init__(self, database):
        self.database = database

    def create(self, nome, quantidade, itens):
        try:
            counter = 0
            for i in itens:
                if Produto.verify(self, i) != []:
                    if counter == 0:
                        query = "MATCH (p:Produto {nome: $item}) CREATE (c:Cliente {nome: $nome})-[:Comprou{quantidade:$quantidade}]->(p)"
                        parameters = {"item": i, "nome": nome, "quantidade": quantidade}
                        self.database.execute_query(query, parameters)
                        counter += 1
                    else:
                        query = "MERGE(c:Cliente{nome: $nome}) MERGE(p:Produto{nome: $item}) CREATE(c)-[:Comprou{quantidade:$quantidade}]->(p)"
                        parameters = {"item": i, "nome": nome, "quantidade": quantidade}
                        self.database.execute_query(query, parameters)
                        counter += 1
                else:
                    return "Produto não existe!"
            return "Cliente criado!"
        except:
            return "Erro ao criar o cliente"

    def read(self, nome):
        try:
            query = "MATCH (c:Cliente {nome: $nome}),(p:Produto) RETURN c.nome as Nome, p.nome as Produto"
            parameters = {"nome": nome}
            return self.database.execute_query(query, parameters)
        except:
            return "Erro ao ler o cliente."

    def update(self, nome, novo_nome):
        try:
            query = "MATCH (c:Cliente {nome: $nome}) SET c.nome = $novo_nome"
            parameters = {"nome": nome, "novo_nome": novo_nome}
            self.database.execute_query(query, parameters)
            return "Cliente atualizado!"
        except:
            return "Erro ao atualizar o cliente"

    def delete(self, nome):
        try:
            query = "MATCH (c:Cliente {nome: $nome}) DETACH DELETE c"
            parameters = {"nome": nome}
            self.database.execute_query(query, parameters)
            return "Cliente deletado!"
        except:
            return "Erro ao deletar o cliente."
