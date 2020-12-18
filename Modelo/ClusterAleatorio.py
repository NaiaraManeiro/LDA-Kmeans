from pandas import np
from scipy.spatial import distance


class ClusterAleatorio:

    def __init__(self, matrixTopics, numClusters):
        self.matrixTopics = matrixTopics
        self.numClusters = numClusters
        self.centroides = None
        self.umbralDistCentroides = 0
        self.distancia = 10000
        self.umbral = False
        self.numIteraciones = 2


    def getCentroids(self):
        """ Devuelve los centroides iniciales para el clustering
                        """
        listaDesordenada = self.matrixTopics.copy()
        np.random.shuffle(listaDesordenada)
        centroides = listaDesordenada[:self.numClusters]
        self.centroides = centroides

    def escogerCentroide(self,instancia,centroides):
            """ Calcula las distancias entre una instancia y los centroides y devuelve el centroide más
                cercano, el número del cluster y la distancia entre el centroide más cercano y la instancia
                                Parámetros:
                                    instancia -- instancia de la matrixTopics
                                    centroides -- array de coordenadas de los centroides
                    """
            distanciaMin=10000000
            indiceMin=0
            centroideCercano=None
            i=0
            distancias=[]
            for centroide in centroides:
                distancia= distance.euclidean(instancia,centroide)
                distancias.append(distancia)
                if distancia<distanciaMin:
                    distanciaMin=distancia
                    centroideCercano=centroide
                    indiceMin=i
                i+=1

            return centroideCercano,indiceMin,distancias

    def generarClusters(self):
            """Devuelve los clusters con sus centroides y las instancias más cercanas, el número de cluster
                de cada instancia y una matriz de las distancias entre los centroides y sus instancias más
                cercanas
                                           """
            self.getCentroids()
            centroidesIniciales=self.centroides
            clusters= {}
            listaClustersInstancias=[]
            matrizDistancias=[]
            for instancia in self.matrixTopics:
                centroide,indice,distancias=self.escogerCentroide(instancia,centroidesIniciales)
                if str(centroide) not in clusters.keys():
                    clusters[str(centroide)]=[]

                clusters[str(centroide)].append(instancia)
                listaClustersInstancias.append(indice)
                matrizDistancias.append(distancias)
            return listaClustersInstancias
