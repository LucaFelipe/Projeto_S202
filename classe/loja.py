class Loja:
    def __init__(self, database):
        self.database = database
        
    def create(self, nome, endereco, lucro_mensal, numero_funcionarios):
        try:
            query = "CREATE(l:Loja{nome:$nome, endereco:$endereco, lucro_mensal:$lucro_mensal, numero_funcionarios:$numero_funcionarios})"
            parameters = {"nome":nome, "endereco":endereco, "lucro_mensal":lucro_mensal, "numero_funcionarios":numero_funcionarios}
            self.database.execute_query(query, parameters)
            return "Loja criada!"
        except:
            return "Erro ao criar a loja!"
        
    def read(self, nome):
        try:
            query = "MATCH (l:Loja {nome: $nome}) RETURN l.nome, l.endereco, l.lucro_mensal, l.numero_funcionarios"
            parameters = {"nome": nome}
            return self.database.execute_query(query, parameters)
        except:
            return "Erro ao ler a loja."
        
    def update(self, nome, novo_nome, novo_endereco, novo_lucro_mensal, novo_numero_funcionarios):
        try:
            query = "MATCH (l:Loja {nome: $nome}) SET l.nome = $novo_nome, l.endereco = $novo_endereco, l.lucro_mensal = $novo_lucro_mensal, l.numero_funcionarios = $novo_numero_funcionarios"
            parameters = {"nome": nome, "novo_nome": novo_nome, "novo_endereco": novo_endereco, "novo_lucro_mensal": novo_lucro_mensal, "novo_numero_funcionarios": novo_numero_funcionarios}
            self.database.execute_query(query, parameters)
            return "Loja atualizada!"
        except:
            return "Erro ao atualizar a loja"
    
    def delete(self, nome):
        try:
            query = "MATCH (l:Loja {nome: $nome}) DETACH DELETE l"
            parameters = {"nome": nome}
            self.database.execute_query(query, parameters)
            return "Loja deletada!"
        except:
            return "Erro ao deletar a loja."
        
    def verify(self, nome):
        query = "MATCH(l:Loja{nome:$nome}) RETURN l.nome as nome"
        parameters = {"nome":nome}
        results = self.database.execute_query(query, parameters)
        return results
