from Graph import *

# See if:
# * Creation of Vertices works;
# * Creation of Edges works;
# * Creation of Graphs works;
# * If everything is showing correctly.
def test_one():
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


# See if it is adding the edge correctly to the graph
def test_two():
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