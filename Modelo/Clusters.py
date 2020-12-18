import random
from scipy.spatial import distance
from Modelo import K_Means, FileHandler
import numpy as np
import collections
import math


def SSE(X,listaClusters, centroides):
    """ Devuelve la suma de errores cuadraticos respecto a los centroides de cada cluster
                        Parámetros:
                            X -- vector de todas las instancias
                            listaCluster -- lista de que instancias pertenecen a que clusters
                            centroides -- lista de los centroides de los clusters
            """

    suma = 0.0
    indice=0
    for instancia in listaClusters:
        centroide=centroides[instancia]
        distancia = distance.euclidean(X[indice], centroide)
        suma += math.pow(distancia,2)
        indice+=1

    return suma


def BSS(listaCluster, X, centroides):
    """ Devuelve la separabilidad de los clusters respecto a los centroides de cada cluster y el
        centroide general.
                    Parámetros:
                        listaCluster -- lista de que instancias pertenecen a que clusters
                        X -- vector de todas las instancias
                        centroides -- lista de los centroides de los clusters
                """

    array = np.array(X)
    centroideCompleto = np.mean(array, axis=0)
    bss = 0.0
    i = 0
    count = collections.Counter(listaCluster)
    for key1 in centroides:
        numInstancias = count[i]
        distancia = distance.euclidean(key1, centroideCompleto)
        bss = bss + (numInstancias * (distancia ** 2))
        i+=1

    return bss


def newNumCluster(X,inicio,fin,salto,almacenar,path,distancia):
    """ Devuelve el número de clusters que va a ser óptimo según los valores de SSE y BSS
                        Parámetros:
                            X -- vector de todas las instancias
                            inicio -- desde que número se quieren mirar los clusters
                            fin -- hasta que número se quieren mirar los clusters
                            salto -- de cuanto en cuanto se van mirando los números
                            almacenar -- boolean para guardar el resultado o no
                            path -- path donde se quiere guardar el resultado
                    """

    iter=0
    resultados=""
    resultadosSSE=[]
    resultadosBSS=[]
    numClusters=[]
    for i in range(inicio,fin,salto):
        numClusters.append(i)
        resultados=resultados+ "Resultados para K="+str(i)+"\n"
        kmeans = K_Means.K_Means(np.array(X), i,distancia)
        listaDistancias, listaClusters, listaCentroides, diccionario = kmeans.k_means()
        sse = SSE(X, listaClusters, listaCentroides)
        bss = BSS(listaClusters, X, listaCentroides)
        resultadosSSE.append(sse)
        resultadosBSS.append(bss)
        resultados+="SSE="+str(sse)+"\t BSS="+str(bss)+"\n\n"
        iter+=1
        if(iter is 9 and almacenar):
            FileHandler.guardarDocumento(resultados,path+"/resultadosHastai="+str(i))
            resultados=""
            iter=0

    if almacenar:
        FileHandler.guardarDocumento(resultados, path + "/resultadosHastai=" + "fin")

    return numClusters,resultadosSSE,resultadosBSS


def generarClusterOptimo(X, iteraciones,numClusters,distancia):
    """ Se calcula el cluster más óptimo según los valores de SSE y BSS obtenidos
                        Parámetros:
                            X -- vector de todas las instancias
                            iteraciones -- cuantas veces se quiere generar el clustering
                    """

    listaDistanciasOptima=[]
    listaPrediccionesOptima=[]
    clustersOpt=[]
    dictOpt={}

    bssOpt=-10000000000000
    sseOpt=100000000000000

    listaBSS=[]
    listaSSE=[]

    for i in range(0,iteraciones):
        kmeans = K_Means.K_Means(X, int(numClusters),distancia)
        listaClusters, clusters=kmeans.k_means()
        sse=SSE(X, listaClusters, clusters)
        bss=BSS(listaClusters, X, clusters)
        listaBSS.append(bss)
        listaSSE.append(sse)
        if (sse<=sseOpt and bss>=bssOpt):
            bssOpt=bss
            sseOpt=sse
            print("Optimo \n")
            print("BSS"+str(bss))
            print("SSE"+str(sse))
            listaPrediccionesOptima=listaClusters
            clustersOpt=clusters


    return listaPrediccionesOptima,clustersOpt,listaBSS,listaSSE


def generarClusterAleatorio(X):
    """ Genera un cluster aleatorio
                        Parámetros:
                            X -- vector de todas las instancias
                    """

    lista = [0] * len(X)
    semilla=100
    for i in range(len(X)):
        random.seed(semilla)
        semilla+=100
        lista[i] = random.randint(0, 70)
    print(collections.Counter(lista))
    return lista

def generarClusterAleatorio2(X,listaClusters):
    """ Genera un cluster aleatorio
                        Parámetros:
                            X -- vector de todas las instancias
                    """
    recuento=dict(collections.Counter(listaClusters))

    lista = [-1] * len(X)
    for indice in recuento.keys():
        numApariciones=recuento[indice]
        i=1
        while i <=numApariciones:
            aleatorio=random.randint(0, len(listaClusters)-1)
            if lista[aleatorio]==-1:
                lista[aleatorio]=indice
                i+=1
    return lista

