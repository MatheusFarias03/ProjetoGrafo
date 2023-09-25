from Graph import *
from os import name, system


class Menu:

  def __init__(self):
    pass

  def show_menu_screen(self):
    # for windows
    if name == 'nt':
      system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
      system('clear')
    print("\n ----- MENU ----- \n")
    print("Q. Ler dados do arquivo grafo.txt;")
    print("W. Gravar dados no arquivo grafo.txt;")
    print("E. Inserir vértice;")
    print("R. Inserir aresta;")
    print("A. Remove vértice;")
    print("S. Remove aresta;")
    print("D. Mostrar conteúdo do arquivo;")
    print("F. Mostrar grafo;")
    print("Z. Apresentar a conexidade do grafo e o reduzido;")
    print("X. Encerrar a aplicação.\n\n")
