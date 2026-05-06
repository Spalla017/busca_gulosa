from vertice import Vertice
from adjacente import Adjacente

class Grafo:
    def __init__(self):
        self.arad = Vertice("Arad", 366)
        self.bucharest = Vertice("Bucharest", 0)
        self.craiova = Vertice("Craiova", 160)
        self.dobreta = Vertice("Dobreta", 242)
        self.fagaras = Vertice("Fagaras", 178)
        self.giurgiu = Vertice("Giurgiu", 77)
        self.lugoj = Vertice("Lugoj", 244)
        self.mehadia = Vertice("Mehadia", 241)
        self.oradea = Vertice("Oradea", 380)
        self.pitesti = Vertice("Pitesti", 98)
        self.rimnicu = Vertice("Rimnicu Vilcea", 193)
        self.sibiu = Vertice("Sibiu", 253)
        self.timisoara = Vertice("Timisoara", 329)
        self.zerind = Vertice("Zerind", 374)

        #Arad
        self.arad.adcAdjacente(Adjacente(self.zerind, 75))
        self.arad.adcAdjacente(Adjacente(self.sibiu, 140))
        self.arad.adcAdjacente(Adjacente(self.timisoara, 118))

        #Zerind
        self.zerind.adcAdjacente(Adjacente(self.arad, 75))
        self.zerind.adcAdjacente(Adjacente(self.oradea, 71))

        #Oradea
        self.oradea.adcAdjacente(Adjacente(self.zerind, 71))
        self.oradea.adcAdjacente(Adjacente(self.sibiu, 151))

        #Timisoara
        self.timisoara.adcAdjacente(Adjacente(self.lugoj, 111))
        self.timisoara.adcAdjacente(Adjacente(self.arad, 118))

        #Sibiu
        self.sibiu.adcAdjacente(Adjacente(self.fagaras, 99))
        self.sibiu.adcAdjacente(Adjacente(self.rimnicu, 80))

        #Lugoj
        self.lugoj.adcAdjacente(Adjacente(self.mehadia, 70))
        self.lugoj.adcAdjacente(Adjacente(self.timisoara, 111))

        #Fagaras
        self.fagaras.adcAdjacente(Adjacente(self.sibiu, 99))
        self.fagaras.adcAdjacente(Adjacente(self.bucharest, 211))

        #Rimnicu
        self.rimnicu.adcAdjacente(Adjacente(self.sibiu, 80))
        self.rimnicu.adcAdjacente(Adjacente(self.pitesti, 97))
        self.rimnicu.adcAdjacente(Adjacente(self.craiova, 146))

        #Mehadia
        self.mehadia.adcAdjacente(Adjacente(self.lugoj, 70))
        self.mehadia.adcAdjacente(Adjacente(self.dobreta, 75))

        #Dobreta
        self.dobreta.adcAdjacente(Adjacente(self.mehadia, 75))
        self.dobreta.adcAdjacente(Adjacente(self.craiova,120))

        #Pitesti
        self.pitesti.adcAdjacente(Adjacente(self.rimnicu, 97))
        self.pitesti.adcAdjacente(Adjacente(self.bucharest, 101))
        self.pitesti.adcAdjacente(Adjacente(self.craiova, 138))

        #Craiova
        self.craiova.adcAdjacente(Adjacente(self.dobreta, 120))
        self.craiova.adcAdjacente(Adjacente(self.rimnicu, 146))
        self.craiova.adcAdjacente(Adjacente(self.pitesti, 138))
        
