from Graph import *
from RappiWebScraper import *
import tests

def main():
    graph = Graph("ProductsRecommender")
    rappi_scraper = RappiWebScraper()
    
    id_num = 1
    wholesalers_vertices = rappi_scraper.get_wholesalers_vertices(id_num=id_num)
    for v in wholesalers_vertices:
        graph.add_vertex(v)
        
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
    
main()