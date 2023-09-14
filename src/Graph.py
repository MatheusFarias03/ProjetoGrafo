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
        """
        Adds a vertex to the graph.

        This function adds a vertex to the graph and updates the adjacency matrix accordingly.
        It checks if the vertex with the same ID already exists in the graph to avoid duplicates.

        :param vertex: The vertex to be added.
        :type vertex: Vertex
        :return: True if the vertex was added successfully, False otherwise.
        :rtype: bool
        """
        
        # Check if the vertex already exists.
        for v in self.vertices:
            if v.id == vertex.id:
                print(f'\nERROR: Vertex with id {vertex.id} already exists in the graph.\n')
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
    
    
    def add_edge(self, edge:Edge) -> bool:
        """
        Adds an edge to the graph.

        This function adds an edge to the graph, and if the vertices
        of the edge don't already exist in the graph, it adds them as well.
        It also checks if the edge with the same ID already exists in the graph.

        :param edge: The edge to be added.
        :type edge: Edge
        :return: True if the edge was added successfully, False otherwise.
        :rtype: bool
        """
        
        # Initialize the postion variables for the vertices.
        from_pos = -1
        to_pos = -1

        # 'i' is the index of the 'v' vertex in the 'vertices' list. This section is basically going
        # to traverse the vertices list and retrieve the index of both vertices so that we can add 
        # an edge to the respective position in the adjacency matrix.
        for i, v in enumerate(self.vertices):
            if edge.from_vertex.id == v.id:
                from_pos = i
            elif edge.to_vertex.id == v.id:
                to_pos = i
        
        # If one of the vertices was not found, create the vertex.
        if from_pos == -1:
            self.add_vertex(edge.from_vertex)
            
        if to_pos == -1:
            self.add_vertex(edge.to_vertex)
        
        # Check if the edge already exists.
        for e in self.edges:
            if e.id == edge.id:
                print(f'\nERROR: Edge with id {edge.id} already exists in the graph.\n')
                return False                
        
        self.edges.append(edge)
        self.num_edges += 1
        
        # Add the edge in the adjacency matrix.
        self.adj_matrix[from_pos][to_pos] = edge
        
        return True
            

    def show_adj_matrix(self):
        """
        Prints the adjacency matrix of the graph.

        This function prints the adjacency matrix of the graph, where each row and column
        represent vertices, and the values in the matrix indicate the presence of edges between
        those vertices. This can be useful for visualizing the graph's structure.

        :return: None
        """
        
        for i in range(self.num_vertices):
            print(self.adj_matrix[i])


