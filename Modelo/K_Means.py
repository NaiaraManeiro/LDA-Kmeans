from time import time
import numpy as np
from Modelo import Distancias


class K_Means:

    def __init__(self, matrixTopics, numClusters, distancia):
        self.matrixTopics = matrixTopics
        self.numClusters = numClusters
        self.centroides =None
        self.umbralDistCentroides=0
        self.distancia=10000
        self.umbral = False
        self.numIteraciones=2
        self.tipoDistancia = distancia


    def getInitialCentroids(self):
        """ Devuelve los centroides iniciales para el clustering
                        """
        listaDesordenada=self.matrixTopics.copy()
        np.random.shuffle(listaDesordenada)
        centroides = listaDesordenada[:self.numClusters]
        self.centroides=centroides
        return centroides

    def escogerCentroide(self,instancia,centroides,):
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
            if (self.tipoDistancia).lower() == "euclidea":
                distancia = Distancias.distanciaEuclidea(instancia,centroide)
            elif (self.tipoDistancia).lower() == "manhatthan":
                distancia = Distancias.distanciaManhattan(instancia, centroide)
            else:
                distancia = Distancias.distanciaEuclidea(instancia, centroide)
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
        return clusters,listaClustersInstancias,np.array(matrizDistancias)

    def generarNuevosCentroides(self,dictClusters):
        """ Devuelve los nuevos centroides de los clusters generados mediante las instancias de dichos
            clusters
                                    Parámetros:
                                        dictClusters -- diccionario formado por clusters, con los
                                        centroides y sus instancias correspondientes
                        """
        listaClusters=[]
        for key in dictClusters.keys():
            lista=dictClusters[key]
            array=np.array(lista)
            clusterNuevo=np.mean(array,axis=0)
            listaClusters.append(clusterNuevo)

        return np.array(listaClusters)

    def compararCentroides(self,centroidesActuales):
        """ Compara los últimos centroides generados con los actuales para ver cuales son mejores y
            devuelve la distancia entre ellos y si los nuevos centroides son buenos o no
                                    Parámetros:
                                        centroidesActuales -- lista de los últimos centroides generados
                        """
        distancia=np.linalg.norm(centroidesActuales-self.centroides)
        seguir=False
        if (abs(distancia-self.distancia)>self.umbralDistCentroides and distancia>0):
            seguir=True
            self.centroides=centroidesActuales
            self.distancia = distancia
        return seguir, distancia

    def k_means(self):
        """ Devuelve el centroide más cercano, una lista de a que cluster pertenece cada instancia, una lista
            de los últimos centroides generados, y un diccionario con los clusters con sus centroides y las
            instancias más cercanas
                        """
        seguir=True
        self.getInitialCentroids()
        clusters,listaClusters,listaDistancias = self.generarClusters()
        i=1
        startTime = time()
        while seguir and i<self.numIteraciones:
            nuevosCentroides=self.generarNuevosCentroides(clusters)
            seguir, distancia =self.compararCentroides(nuevosCentroides)

            if i == 2:
                if not self.umbral:
                    self.umbralDistCentroides = abs(distancia - distanciaAnterior) / 1000
                    self.umbral = True

            if seguir:
                clusters, listaClusters, listaDistancias = self.generarClusters()
                distanciaAnterior = self.distancia
                i += 1
            if i==1:
                tiempoPasado = time() - startTime
                self.numIteraciones=int(1800/tiempoPasado)

        return listaClusters, np.array(nuevosCentroides)
        # listaDistancias = transform
        # listaClusters = predict
        # clusters = diccionario

    # def predict(self,instancia):
    #     centroides,i,distancias=self.escogerCentroide(instancia,self.centroides)
    #     return i