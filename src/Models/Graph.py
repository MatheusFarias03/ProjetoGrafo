class Vertex:
    """
    Vertices symbolize entities or data points.
    """

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
        
    def show_all(self):
        print(f'Vertex >> id:{self.id}; properties:{self.properties}; label:{self.label}')


class Edge:
    """
    Edges connect vertices and represent the relationship between them.
    """

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


class Graph:

    def __init__(self, name:str):
        self.name = name
        self.num_vertices = 0
        self.num_edges = 0
        self.vertices = []
        self.edges = []
        self.adj_matrix = []

    def add_vertex(self, vertex:Vertex):
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
                return [-1] # If it does, return an array with -1 to represent that the vertex already exists.
            
            if v.properties['name'] == vertex.properties['name'] and v.label == 'Product':
                return [0, v] # If there is one product that already exists, return it as the second element.

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

        return [0] # This means that the vertex was added.
    
    
    def add_edge(self, edge:Edge) -> bool:
        """
        Adds an edge to the graph.

        This function adds an edge to the graph. 
        
        The vertices must have been created before adding the edge.
        
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
        
        # If one of the vertices was not found, print an errro saying it is necessart to create the vertex.
        if from_pos == -1:
            print(f'''
                  \nERROR: from_pos vertex was not added to the graph.\n 
                  Hint: use <graph>.add_vertex(<from_pos>)\n
                  ''')
            return False
        
        if to_pos == -1:
            print(f'''
                  \nERROR: to_pos vertex was not added to the graph.\n 
                  Hint: use <graph>.add_vertex(<from_pos>)\n
                  ''')
            return False
        
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

        :return: None
        """
        
        for i in range(self.num_vertices):
            print(self.adj_matrix[i])


    def get_vertex_outgoing_edges(self, vertex_props:dict, label:str='_ag_label_vertex') -> list:
        """
        Retrieves outgoing edges from vertices that match specified properties and label.

        :param vertex_props: A dictionary of properties to match in vertices.
        :type vertex_props: dict
        :param label: (Optional) The label to match for vertices. Default is '_ag_label_vertex'.
        :type label: str
        :return: A list of outgoing edges from matching vertices.
        :rtype: list
        """
        
        # List for the position of the corresponding vertices in the adjacency matrix.
        vertices_pos = []
        edges_list = []
        
        # Traverse the vertices list. For each vertex we see if there is a sequence of values in their
        # 'properties' dictionary that matches the given criteria in the 'vertex_props' dictionary.
        # All the key-value pairs need to match. If it was provided the 'label' of the vertex, it needs
        # to match as well.
        for i, v in enumerate(self.vertices):
            num_matches = 0
            for k in vertex_props:
                if k in v.properties.keys():
                    if vertex_props[k] == v.properties[k]:
                        if label != '_ag_label_vertex' and v.label == label:
                            num_matches += 1
                        elif label == '_ag_label_vertex':
                            num_matches += 1
            
            if num_matches == len(vertex_props):
                vertices_pos.append(i)
        
        for i in vertices_pos:
            for j in self.adj_matrix[i]:
                if j != 0:
                    edges_list.append(j)
                    
        return edges_list