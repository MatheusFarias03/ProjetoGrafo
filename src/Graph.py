class Vertex:

  def __init__(self,
               id: int,
               properties: dict,
               label: str = '_ag_label_vertex'):
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
    print(
        f'Vertex >> id:{self.id}; properties:{self.properties}; label:{self.label}'
    )


class Edge:

  def __init__(self,
               id: int,
               from_vertex: Vertex,
               to_vertex: Vertex,
               properties: dict,
               label: str = '_ag_label_edge'):
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
    print(
        f'Edge >> id:{self.id}; properties:{self.properties}; label:{self.label}; from_vertex.id: {self.from_vertex.id}; to_vertex_id: {self.to_vertex.id}'
    )

  def show_from_vertex(self):
    self.from_vertex.show_all()

  def show_to_vertex(self):
    self.to_vertex.show_all()


class Graph:

  def __init__(self, name: str):
    self.name = name
    self.num_vertices = 0
    self.num_edges = 0
    self.vertices = []
    self.edges = []
    self.adj_matrix = []

  def add_vertex(self, vertex: Vertex) -> bool:
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
        print(
            f'\nERROR: Vertex with id {vertex.id} already exists in the graph.\n'
        )
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
      for i in range(0, self.num_vertices - 1):
        self.adj_matrix[i].append(0)
      self.adj_matrix.append([])
      for j in range(0, self.num_vertices):
        self.adj_matrix[-1].append(0)

    return True

  def add_edge(self, edge: Edge) -> bool:
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
        print(
            f'\nERROR: Edge with id {edge.id} already exists in the graph.\n')
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

  def get_vertex_outgoing_edges(self,
                                vertex_props: dict,
                                label: str = '_ag_label_vertex') -> list:
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

  def read_file(self):
    with open('grafo.txt', 'r') as file:
      for line in file:
        parts = line.strip().split(';')

        if parts[0] == 'v':
          vertex_id = int(parts[1])
          vertex_data = eval(parts[2])
          vertex_label = parts[3]
          vertex_data['name'] = vertex_data['name'].replace("'", "")

          vertex = Vertex(vertex_id, vertex_data, vertex_label)
          self.add_vertex(vertex)

        if parts[0] == 'e':
          edge_id = int(parts[1])
          edge_data = eval(parts[2])
          edge_label = parts[3]
          source_vertex_id = int(parts[4])
          target_vertex_id = int(parts[5])

          for v in self.vertices:
            if v.id == source_vertex_id:
              from_vertex = v
            if v.id == target_vertex_id:
              to_vertex = v

          edge = Edge(edge_id, from_vertex, to_vertex, edge_data, edge_label)
          self.add_edge(edge)
    file.close()

  def remove_vertex(self, id):
    try:
      for i, v in enumerate(self.vertices):
        if v.id == id:
          pos = i
          self.vertices.pop(pos)

      edges = 0
      for i in range(self.num_vertices):
        for j in range(self.num_vertices):
          if (i == pos or j == pos) and self.adj_matrix[i][j] != 0:
            edges += 1

      self.adj_matrix.pop(pos)
      for line in self.adj_matrix:
        line.pop(pos)
      self.num_edges -= edges
      self.num_vertices -= 1
    except Exception as e:
      print(e)

  def remove_edge(self, id):
    try:
      for i, e in enumerate(self.edges):
        if e.id == id:
          pos = i
          self.edges.pop(pos)

      for i in range(self.num_vertices):
        for j in range(self.num_vertices):
          if self.adj_matrix[i][j].id == id:
            self.adj_matrix[i][j] = 0

    except Exception as e:
      print(e)

  def is_strongly_connected(self) -> bool:
    """
          Verifica se o grafo é fortemente conexo usando busca em profundidade.
          :return: True se for fortemente conexo, False caso contrário.
          """
    for vertex in self.vertices:
      visited = set()
      self._dfs(vertex, visited)

      # Verifica se todos os vértices foram visitados
      if len(visited) != self.num_vertices:
        return False

    return True

  def _dfs(self, start_vertex: Vertex, visited: set):
    """
      Função de busca em profundidade recursiva.
      """
    visited.add(start_vertex.id)
    for neighbor in self.get_neighbors(start_vertex):
      if neighbor.id not in visited:
        self._dfs(neighbor, visited)

  def get_neighbors(self, vertex: Vertex):
    """
      Obtém os vértices vizinhos de um vértice.
      """
    neighbors = []
    index = self.vertices.index(vertex)

    for i in range(self.num_vertices):
      if self.adj_matrix[index][
          i] != 0:  # vertex.id nao corresponde ao indice na matrix de adjacencia.
        neighbors.append(self.vertices[i])
    return neighbors

  def is_semi_strongly_connected(self) -> bool:
    """
          Verifica se o grafo é semi-fortemente conexo usando busca em profundidade.
          :return: True se for semi-fortemente conexo, False caso contrário.
          """
    for v in self.vertices:
      for w in self.vertices:
        if v != w:
          if not self._has_path(v, w) and not self._has_path(w, v):
            return False
    return True

  def _has_path(self, start_vertex: Vertex, target_vertex: Vertex) -> bool:
    """
      Verifica se há um caminho entre dois vértices usando busca em profundidade.
      """
    visited = set()
    stack = [start_vertex]

    while stack:
      current_vertex = stack.pop()
      visited.add(current_vertex.id)

      if current_vertex == target_vertex:
        return True

      for neighbor in self.get_neighbors(current_vertex):
        if neighbor.id not in visited:
          stack.append(neighbor)

    return False

  def is_disconnected(self) -> bool:
    """
        Verifica se o grafo é desconexo usando busca em largura.
        :return: True se for desconexo, False caso contrário.
        """
    visited = set()

    for vertex in self.vertices:
      if vertex.id not in visited:
        self._dfs(vertex, visited)

    if len(visited) == self.num_vertices:
      return False
    return True

  def check_graph_category(self):
    """
      Verifica a categoria de um grafo direcionado com base nos métodos is_strongly_connected,is_semi_strongly_connected e is_disconnected.
      :return: A categoria do grafo (C0, C1, C2, ou C3).
    """
    category = "C3"  # Inicialmente, assume-se que o grafo é fortemente conexo (C3).

    if not self.is_strongly_connected(
    ):  # Verifica se é fortemente conexo (C3).
      category = "C2"

      if not self.is_semi_strongly_connected(
      ):  # Verifica se é semi-fortemente conexo (C2).
        category = "C0"

        if not self.is_disconnected():  # Verifica se é desconexo (C0).
          category = "C1"

    return category

 

  def grafo_reduzido(self):
    vertices_checados = []
    grafo_reduzido = Graph('GrafoReduzido')
    vertices_grafo_reduzido = []

    for i in range(self.num_vertices):
      v = self.vertices[i]
      if v in vertices_checados:
        continue

      lista_R_pos = [v]
      lista_R_neg = [v]
      lista_R = [v]

      if v not in vertices_checados:
        vertices_checados.append(v)

      for w in self.vertices:
        both_found = 0
        if self._has_path(v, w) == True:
          lista_R_pos.append(w)
          both_found += 1

        if self._has_path(w, v) == True:
          lista_R_neg.append(w)
          both_found += 1

        if both_found == 2:
          lista_R.append(w)
          if w not in vertices_checados:
            vertices_checados.append(w)

      novo_vertice = Vertex(id=i, properties={'Vertices': []})

      for k in lista_R:
        novo_vertice.properties['Vertices'].append(k)
      vertices_grafo_reduzido.append(novo_vertice)


    k = 0
    for v in vertices_grafo_reduzido:
      grafo_reduzido.add_vertex(v)
      for w in vertices_grafo_reduzido:
        if w not in grafo_reduzido.vertices:
          grafo_reduzido.add_vertex(w)
        for i in v.properties['Vertices']:
          for j in w.properties['Vertices']:
            if self._has_path(i, j):
              e = Edge(k, v, w, {}, 'Edge')
              grafo_reduzido.add_edge(e)
              k += 1
    grafo_reduzido.show_adj_matrix()
