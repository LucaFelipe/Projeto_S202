class Loja:
    def __init__(self, database):
        self.database = database
        
    def create(self, nome, endereco, lucro_mensal):
        try:
            query = "CREATE(l:Loja{nome:$name, endereco:$endereco, lucro_mensal:$lucro_mensal})"
            parameters = {"name":nome, "endereco":endereco, "lucro_mensal":lucro_mensal}
            self.database.execute_query(query, parameters)
            return "Loja criada!"
        except:
            return "Erro ao criar a loja!"
        
    def verify(self, nome):
        query = "MATCH(l:Loja{nome:$nome}) RETURN l.name as name"
        parameters = {"nome":nome}
        results = self.database.execute_query(query, parameters)
        return results