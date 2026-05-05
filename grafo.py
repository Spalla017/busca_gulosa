from Vertice import Vertice
from Adjacente import Adjacente

class Grafo:
    def __init__(self):
        # Vértices
        self.arad = Vertice("Arad", 366)
        self.bucharest = Vertice("Bucharest", 0)
        self.craiova = Vertice("Craiova", 160)
        self.dobreta = Vertice("Dobreta", 242)
        self.eforie = Vertice("Eforie", 161)
        self.fagaras = Vertice("Fagaras", 178)
        self.giurgiu = Vertice("Giurgiu", 77)
        self.hirsova = Vertice("Hirsova", 151)
        self.iasi = Vertice("Iasi", 226)
        self.lugoj = Vertice("Lugoj", 244)
        self.mehadia = Vertice("Mehadia", 241)
        self.neamt = Vertice("Neamt", 234)
        self.oradea = Vertice("Oradea", 380)
        self.pitesti = Vertice("Pitesti", 98)
        self.rimnicu = Vertice("Rimnicu Vilcea", 193)
        self.sibiu = Vertice("Sibiu", 253)
        self.timisoara = Vertice("Timisoara", 329)
        self.urziceni = Vertice("Urziceni", 80)
        self.vaslui = Vertice("Vaslui", 199)
        self.zerind = Vertice("Zerind", 374)

        # Conexões
        # Arad
        self.arad.adicionar_adjacente(Adjacente(self.zerind, 75))
        self.arad.adicionar_adjacente(Adjacente(self.sibiu, 140))
        self.arad.adicionar_adjacente(Adjacente(self.timisoara, 118))

        # Zerind
        self.zerind.adicionar_adjacente(Adjacente(self.arad, 75))
        self.zerind.adicionar_adjacente(Adjacente(self.oradea, 71))
