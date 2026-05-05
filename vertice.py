class vertice:
    def __init__(self, rotulo, distancia):
        self.rotulo = rotulo
        self.distancia = distancia
        self.visitado = False  
        self.adjacentes = []

    def adcAdjacente(self, vertice):
        self.adjacentes.append(vertice)

    def exibir_adjacentes(self):
        for i, adj in enumerate(self.adjacentes):
            print(i, "-", adj.vertice.nome, "-", adj.custo)
