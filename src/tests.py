from Models.Graph import *
from Models.RappiWebScraper import *


def vertex_creation():
    """
    See if:
        Creation of Vertices works;\n
        Creation of Edges works;\n
        Creation of Graphs works;\n
        If everything is showing correctly.\n
    """
    vertex_a = Vertex(1, {'name': 'vertex_a'})
    vertex_b = Vertex(2, {'name': 'vertex_b'})
    vertex_c = Vertex(3, {'name': 'vertex_c'})
    edge_a_b = Edge(4, vertex_a, vertex_b, {'name': 'edge_a_b'})
    graph = Graph('TheGraph')

    edge_a_b.show_id()
    edge_a_b.show_label()
    edge_a_b.show_properties()
    edge_a_b.show_from_vertex()
    edge_a_b.show_to_vertex()
    graph.show_adj_matrix()
    graph.add_vertex(vertex_a)
    graph.show_adj_matrix()
    graph.add_vertex(vertex_b)
    graph.show_adj_matrix()
    graph.add_vertex(vertex_c)
    graph.show_adj_matrix()



def edge_insertion():
    """
    See if it is adding the edge correctly to the graph
    """
    vertex_a = Vertex(1, {'name': 'vertex_a'})
    vertex_b = Vertex(2, {'name': 'vertex_b'})
    vertex_c = Vertex(3, {'name': 'vertex_c'})
    
    edge_a_b = Edge(4, vertex_a, vertex_b, {'name': 'edge_a_b'})
    edge_b_c = Edge(5, vertex_b, vertex_c, {'name': 'edge_b_c'})
    
    graph = Graph('TheGraph')
    
    graph.add_vertex(vertex_a)
    graph.add_vertex(vertex_b)
    graph.add_vertex(vertex_c)
    
    graph.add_edge(edge_a_b)
    graph.add_edge(edge_b_c)
    
    graph.show_adj_matrix()
    my_list = graph.get_vertex_outgoing_edges({'name': 'vertex_a'})
    print(f'my_list: {my_list}')
    
    
    
def webscraping_insertion():
    """
    See if webscraping, and adding data from web to graph works.
    """
    graph = Graph("ProductsRecommender")
    rappi_scraper = RappiWebScraper()
    
    id_num = 1
    wholesalers_vertices = rappi_scraper.get_wholesalers_vertices(id_num=id_num)
    for v in wholesalers_vertices:
        graph.add_vertex(v)
    
    id_num += len(wholesalers_vertices)
    graph.show_adj_matrix()
    
    rappi_scraper.get_wholesalers_fish(wholesalers_vertices, id_num, graph)
    
    f = open("graph_vertices_and_edges.txt", "w")
    
    for v in graph.vertices:
        v.show_all()
        f.write(f"v;{v.id};{v.properties};{v.label}\n")
    
    for e in graph.edges:
        e.show_all()
        f.write(f"e;{e.id};{e.properties};{e.label};{e.from_vertex.id};{e.to_vertex.id}\n")
        
    print(f'\nNum Vertices: {graph.num_vertices}\nNum Edges: {graph.num_edges}')
    f.close()
    


def file_reading(vertices:list, edges:list, file_name:str):

    with open(file_name, 'r') as file:
        for line in file:
            
            parts = line.strip().split(';')
            
            if parts[0] == 'v':
                vertex_id = int(parts[1])
                vertex_data = eval(parts[2])
                vertex_label = parts[3]
                #vertices.append({'vertex_id': vertex_id, 'data': vertex_data, 'label': vertex_label})
                print(vertex_data['name'])
            
            elif parts[0] == 'e':
                edge_id = int(parts[1])
                edge_data = eval(parts[2])
                edge_label = parts[3]
                source_vertex_id = int(parts[4])
                target_vertex_id = int(parts[5])
                edges.append({'id': edge_id, 'data': edge_data, 'label': edge_label, 'source': source_vertex_id, 'target': target_vertex_id})

    # for v in vertices:
    #     print(v)
        
    # for e in edges:
    #     print(e)
