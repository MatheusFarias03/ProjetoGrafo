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
        
    def show_all(self):
        print(f'Vertex >> id:{self.id}; properties:{self.properties}; label:{self.label}')
