class Vertex:

    def __init__(self, id:int, properties:dict, label:str='_ag_label_vertex'):
        self.id = id
        self.properties = properties
        self.label = label

    def show_id(self):
        print(f'id: {self.id}')

    def show_label(self):
        print(f'label: {self.label}')

    def show_properties(self):
        print(f'properties: {self.properties}')


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

    def show_from_vertex(self):
        self.from_vertex.show_id()
        self.from_vertex.show_label()
        self.from_vertex.show_properties()

    def show_to_vertex(self):
        self.to_vertex.show_id()
        self.to_vertex.show_label()
        self.to_vertex.show_properties()


class Graph:

    def __init__(self, name:str):
        self.name = name
        self.num_vertices = 0
        self.num_edges = 0
        self.vertices = []
        self.edges = []
        self.adj_matrix = []

    def add_vertex(self, vertex:Vertex) -> bool:
        # Check if the vertex already exists.
        for v in self.vertices:
            if v.id == vertex.id:
                print(f'Vertex with id {vertex.id} already exists in the graph.')
                return False

        self.vertices.append(vertex)
        self.num_vertices += 1

        # When we add the first vertex, create only one list containing a 0.
        if self.num_vertices == 1:
            self.adj_matrix.append([0])

        # If we have more than one vertex, add a 0 for every existing row, mimicking the creation
        # of a new column. Also create an array with N zeros (with N being the number of vertices)
        # to represent the new row for the created vertex.
        else:
            for i in range(0, self.num_vertices-1):
                self.adj_matrix[i].append(0)
            self.adj_matrix.append([])
            for j in range(0, self.num_vertices):
                self.adj_matrix[-1].append(0)

        return True

    def show_adj_matrix(self):
        for i in range(self.num_vertices):
            print(self.adj_matrix[i])


