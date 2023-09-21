import psycopg2
import age

# Remember to change this to your local settings.
GRAPH_NAME = "TeoriaGrafos"
conn = psycopg2.connect(host="localhost", port="5432", dbname="demo", user="user", password="password")

class Database:
    
    def __init__(self):
        age.setUpAge(conn, GRAPH_NAME)
    
                
    def insert_all_from_file(self):
        vertices = []
        edges = []
        
        with open("graph_vertices_and_edges.txt", 'r') as file:
            
            with conn.cursor() as cursor:
            
                for line in file:
                
                    parts = line.strip().split(';')
                    
                    if parts[0] == 'v':
                        vertex_id = int(parts[1])
                        vertex_data = eval(parts[2])
                        vertex_label = parts[3]
                        
                        vertex_data['name'] = vertex_data['name'].replace("'", "")

                        if vertex_label == "Wholesaler":
                            try:
                                cursor.execute("""
                                            SELECT * FROM cypher(%s, $$
                                            CREATE (n:Wholesaler {id: %s, name: %s, link: %s})
                                            $$) AS (a agtype);
                                            """, (GRAPH_NAME, vertex_id, vertex_data['name'], vertex_data['link']))
                                conn.commit()
                                
                            except Exception as ex:
                                print(type(ex), ex)
                                conn.rollback()
                                
                        elif vertex_label == "Product":
                            try:
                                cursor.execute("""
                                            SELECT * FROM cypher(%s, $$
                                                CREATE (n:Product {id: %s, name: %s, description: %s})
                                            $$) AS (a agtype);
                                            """, (GRAPH_NAME, vertex_id, vertex_data['name'], vertex_data['description']))
                                conn.commit()
                            
                            except Exception as ex:
                                print(type(ex), ex)
                                conn.rollback()
                        
                    
                    if parts[0] == 'e':
                        edge_id = int(parts[1])
                        edge_data = eval(parts[2])
                        edge_label = parts[3]
                        source_vertex_id = int(parts[4])
                        target_vertex_id = int(parts[5])
                        
                        if edge_label == "OFFERS":
                            try:
                                cursor.execute("""
                                               SELECT * FROM cypher(%s, $$
                                                   MATCH (a:Wholesaler {id: %s}), (b:Product {id: %s})
                                                   CREATE (a)-[e:OFFERS {id: %s, price: %s}]->(b)
                                               $$) AS (edge agtype);
                                               """, (GRAPH_NAME, source_vertex_id, target_vertex_id, edge_id, edge_data['price']))
                                conn.commit()
                                
                            except Exception as ex:
                                print(type(ex), ex)
                                conn.rollback()
        
