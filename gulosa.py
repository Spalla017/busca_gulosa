from vertice import Vertice

class Gulosa:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def busca(self, atual):

        print("Vertice Atual: ", atual.rotulo)
        if atual == self.objetivo or atual.distancia == 0:
            self.encontrado = True
            print("Você chegou ao destino!")
            return

        mlhrAdj = None

        for adj in atual.adjacentes:
            if not adj.vertice.visitado:
                if mlhrAdj is None or adj.vertice.distancia < mlhrAdj.vertice.distancia:
                    mlhrAdj = adj

        if mlhrAdj is not None:
            mlhrAdj.vertice.visitado = True
            self.busca(mlhrAdj.vertice)
