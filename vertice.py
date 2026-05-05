class vertice:
    def __init__(self, rotulo, distancia):
        self.rotulo = rotulo
        self.distancia = distancia
        self.visitado = False  
        self.adjacentes = []

    def adcAdjacente(self, vertice):
        self.adjacentes.append(vertice)
    
    

    def getNome(self):
        return self.nome
    def setNome(self, nome):
        self.nome = nome
    
    def getDistancia(self):
        return self.distancia
    def setDistancia(self, distancia):
        self.distancia = distancia
    
    def getVisitado(self):
        return self.visitado
    def setVisitado(self, visitado):
        self.visitado = visitado
    
    def getAdjacentes(self):
        return self.adjacentes
    def setAdjacentes(self, adjacentes):
        self.adjacentes = adjacentes
