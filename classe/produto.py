from classe.loja import Loja

class Produto:
    def __init__(self, database):
        self.database = database
    
    def create(self, nome, preco, data_validade, nome_loja):
        if Loja.verify(self, nome_loja) != []:
            try:
                query = "MATCH (l:Loja {nome: $nome_loja}) CREATE (p:Produto {nome: $nome, preco: $preco, data_validade: $data_validade})-[:Pertence]->(l)"
                parameters = {"nome": nome, "preco":preco, "data_validade":data_validade, "nome_loja":nome_loja}
                self.database.execute_query(query, parameters)
                return "Produto criado!"
            except:
                return "Erro ao criar o produto"
        else:
            return "Loja não existe!"
        
    def read(self, nome):
        try:
            query = "MATCH (p:Produto {nome: $nome}) RETURN p.nome, p.preco, p.data_validade"
            parameters = {"nome": nome}
            return self.database.execute_query(query, parameters)
        except:
            return "Erro ao ler o produto."
        
    def update(self, nome, novo_nome, novo_preco):
        try:
            query = "MATCH (p:Produto {nome: $nome}) SET p.nome = $novo_nome, p.preco = $novo_preco"
            parameters = {"nome": nome, "novo_nome":novo_nome, "novo_preco": novo_preco}
            self.database.execute_query(query, parameters)
            return "Produto atualizado!"
        except:
            return "Erro ao atualizar o produto"
    
    def delete(self, nome):
        try:
            query = "MATCH (p:Produto {nome: $nome}) DETACH DELETE p"
            parameters = {"nome": nome}
            self.database.execute_query(query, parameters)
            return "Produto deletado!"
        except:
            return "Erro ao deletar o produto."
        
    def verify(self, nome):
        query = "MATCH(p:Produto{nome:$nome}) RETURN p.nome as nome"
        parameters = {"nome":nome}
        results = self.database.execute_query(query, parameters)
        return results
