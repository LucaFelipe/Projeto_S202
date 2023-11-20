from neo4j import GraphDatabase, basic_auth

class Database:

    def __init__(self):
        try:
            self.driver = GraphDatabase.driver("bolt://52.90.34.23:7687", auth=basic_auth("neo4j", "miner-inches-departure"))
        except:
            print("Erro ao conectar com o bd!")

    def close(self):
        self.driver.close()
        
    def execute_query(self, query, parameters=None):
        data = []
        with self.driver.session() as session:
            results = session.run(query, parameters)
            for record in results:
                data.append(record)
            return data
        
    def drop_all(self):
        with self.driver.session() as session:
            session.run("MATCH(n) DETACH DELETE n")