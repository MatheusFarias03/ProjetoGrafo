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
    
    fish_vertices = rappi_scraper.get_wholesalers_fish(wholesalers_vertices, id_num)
    for v in fish_vertices:
        graph.add_vertex(v)
        
    graph.show_adj_matrix()
main()