nodes=[]
queue=[]

class node:
    def __init__(self, name,id):
        self.name = name
        self.id= id
        self.visited = False
        self.adjacent = []
        self.parent = None
        self.level = 0
        nodes.append(self)
        self.c='black'


    def addEdge(self, v):
        self.adjacent.append(v)
        self.c='blue'
        v.parent=self
        v.level=self.level+1

