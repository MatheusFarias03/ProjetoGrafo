from Models.Graph import Graph
from Models.Menu import Menu
from Models.Vertex import Vertex
from Models.Edge import Edge

# 3.a [x] Ler dados do arquivo grafo.txt;
# 3.b [x] Gravar dados no arquivo
# 3.c [x] Inserir vértice
# 3.d [x] Inserir aresta
# 3.e [x] Remove vértice
# 3.f [x] Remove aresta
# 3.g [x] Mostrar conteúdo do arquivo
# 3.h [x] Mostrar grafo
# 3.i [] Apresentar a conexidade do grafo e o reduzido
# 3.j [x] Encerrar a aplicação.


def main():

  running = True
  graph = Graph("WholesalersProducts")
  menu = Menu()

  while running == True:
    menu.show_menu_screen()
    option = input("Enter option: ").upper()

    # 3.a. Ler dados do arquivo.
    if option == 'Q':
      graph.read_file()
      print("File read successfully.")
      input("Press enter to continue.")

    # 3.b Escrever dados no arquivo.
    if option == 'W':
      with open('grafo.txt', 'a') as file:
        for v in graph.vertices:
          file.write(f"v;{v.id};{v.properties};{v.label}")
        for e in graph.edges:
          file.write(
              f"e;{e.id};{e.properties};{e.label};{e.from_vertex.id};{e.to_vertex.id}"
          )
      file.close()

    # 3.c. Inserir vértice
    if option == 'E':
      try:
        vertex_id = int(input("Type the vertex id: "))
      except Exception as e:
        print(e)
        input("Press enter to continue.")
        continue

      vertex_label = input("Type the vertex label: ")

      insert_prop = True
      vertex_properties = {}
      while insert_prop:
        try:
          choice = input("Do you want to insert a property? (Y/N): ").upper()

          if choice == 'Y':
            key = input("Type the key: ")
            value = input("Type the value: ")
            vertex_properties[key] = value

          elif choice == 'N':
            insert_prop = False

          else:
            print(f"{choice} is not an option...")
        except Exception as e:
          print(e)
          insert_prop = False
          input("Press enter to continue.")

      vertex = Vertex(vertex_id, vertex_properties, vertex_label)
      graph.add_vertex(vertex)
      input("Press enter to continue.")

    # Inserir aresta.
    if option == 'R':
      try:
        edge_id = int(input("Type the edge id: "))
        source_vertex_id = int(
            input("Type the id of the vertex where the edge comes from: "))
        target_vertex_id = int(
            input("Type the id of the vertex where the edge goes to: "))
      except Exception as e:
        print(e)
        input("Press enter to continue.")
        continue

      edge_label = input("Type the edge label: ")

      insert_prop = True
      edge_properties = {}
      while insert_prop:
        try:
          choice = input("Do you want to insert a property? (Y/N): ").upper()

          if choice == 'Y':
            key = input("Type the key: ")
            value = input("Type the value: ")
            edge_properties[key] = value

          elif choice == 'N':
            insert_prop = False

          else:
            print(f"{choice} is not an option...")
        except Exception as e:
          print(e)
          insert_prop = False
          input("Press enter to continue.")

      for v in graph.vertices:
        if v.id == source_vertex_id:
          from_vertex = v
        if v.id == target_vertex_id:
          to_vertex = v
      try:
        edge = Edge(edge_id, from_vertex, to_vertex, edge_properties,
                    edge_label)
      except Exception as e:
        print(e)
        input("Press enter to continue.")
        continue

      graph.add_edge(edge)
      input("Press enter to continue.")

    # 3.e. Remove vertice.
    if option == 'A':
      try:
        id = int(input("Remove vertex with id: "))
        graph.remove_vertex(id)
        input("Press enter to continue.")
      except Exception as e:
        print(e)
        input("Press enter to continue.")

    # 3.f. Remove aresta.
    if option == 'S':
      try:
        id = int(input("Remove edge with id: "))
        graph.remove_edge(id)
        input("Press enter to continue.")
      except Exception as e:
        print(e)
        input("Press enter to continue.")

    # 3.g. Mostrar conteudo do arquivo.
    if option == 'D':
      with open('grafo.txt', 'r') as file:
        for line in file:
          print(line)

      input("Press enter to continue.")
      file.close()

    # 3.h. Mostrar grafo.
    if option == 'F':
      key_option = input("Which edge key to show? >> ")

      graph.show_adj_matrix(key_option)

      input("\nPress enter to continue.")

    # 3.i. Apresentar a conexidade do grafo e o reduzido.
    if option == 'Z':
      graph_category = graph.check_graph_category()
      print(f"A categoria do grafo é: {graph_category}")
      graph.grafo_reduzido()
      input("Press enter to continue.")

    # 3.j. Encerrar aplicacao.
    if option == 'X':
      running = False

    # Coloracao
    if option == 'C':
      graph.sequential_graph_coloring()
      input("\nPress enter to continue.")

    # Dijkstra
    if option == 'V':
        v1 = Vertex(1, {}, 'varejista')
        v2 = Vertex(2, {}, 'varejista')
        v3 = Vertex(3, {}, 'varejista')
        v4 = Vertex(4, {}, 'produto')
        v5 = Vertex(5, {}, 'produto')
        v6 = Vertex(6, {}, 'produto')

        graph.add_vertex(v1)
        graph.add_vertex(v2)
        graph.add_vertex(v3)
        graph.add_vertex(v4)
        graph.add_vertex(v5)
        graph.add_vertex(v6)

        edge4 = Edge(7, v1, v4, {'price': 27.90}, 'e')
        edge5 = Edge(8, v2, v4, {'price': 32.90}, 'e')
        edge6 = Edge(9, v3, v4, {'price': 30.90}, 'e')
        edge7 = Edge(10, v1, v5, {'price': 7.49}, 'e')
        edge8 = Edge(11, v2, v5, {'price': 8.79}, 'e')
        edge9 = Edge(12, v3, v5, {'price': 8.29}, 'e')
        edge10 = Edge(13, v1, v6, {'price': 4.69}, 'e')
        edge11 = Edge(14, v2, v6, {'price': 4.29}, 'e')
        edge12 = Edge(15, v3, v6, {'price': 4.75}, 'e')

        graph.add_edge(edge4)
        graph.add_edge(edge5)
        graph.add_edge(edge6)
        graph.add_edge(edge7)
        graph.add_edge(edge8)
        graph.add_edge(edge9)
        graph.add_edge(edge10)
        graph.add_edge(edge11)
        graph.add_edge(edge12)

        src = input("Type the source vertex position >> ")
        key = input("Which edge key to analyze? >> ")
        graph.dijkstra(src, key)
        input("\nPress enter to continue.")


main()