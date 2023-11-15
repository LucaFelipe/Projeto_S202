from neo4j import GraphDatabase, basic_auth

class Database:

    def __init__(self):
        self.driver = GraphDatabase.driver("bolt://3.222.117.209:7687", auth=basic_auth("neo4j", "bundles-teeth-winding"))

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