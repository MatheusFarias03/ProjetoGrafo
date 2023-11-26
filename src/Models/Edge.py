from .Vertex import Vertex

class Edge:
    def __init__(self, id:int, from_vertex:Vertex, to_vertex:Vertex, properties:dict, label:str='_ag_label_edge'):
        self.id = id
        self.label = label
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.properties = properties

    def show_id(self):
        print(f'id: {self.id}')

    def show_properties(self):
        print(f'properties: {self.properties}')

    def show_label(self):
        print(f'label: {self.label}')
        
    def show_all(self):
        print(f'Edge >> id:{self.id}; properties:{self.properties}; label:{self.label}; from_vertex.id: {self.from_vertex.id}; to_vertex_id: {self.to_vertex.id}')

    def show_from_vertex(self):
        self.from_vertex.show_all()

    def show_to_vertex(self):
        self.to_vertex.show_all()
