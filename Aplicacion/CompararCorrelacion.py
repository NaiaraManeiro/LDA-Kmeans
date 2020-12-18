from statistics import mean
import sys
sys.path.append("..")

from Modelo import Clusters, ClusterAleatorio, Visualizacion
import numpy as np
from Modelo import AnalyzeResults, FileHandler, K_Means

if __name__ == "__main__":

    if (len(sys.argv)-1!=4):
        print("Ejecutable que compara la correlación de un cluster con un cluster aleatorio ")
        print("El ejecutable tiene que ser llamado con tres argumentos: ")
        print("Ha sido llamado con: " + str(len(sys.argv) - 1))
        print("Argumento 1: path del archivo preprocesado que contiene los topics de los documentos")
        print("Argumento 2: archivo preprocesado con las etiquetas del conjunto")
        print("Argumento 3: objeto que contiene la lista de los clusters a los que pertenecen las instancias")
        print("Argumento 4: directorio en el que almacenar los valores de correlación y los gráficos")
    else:

        X=FileHandler.cargarObjeto(sys.argv[1])

        tags=FileHandler.cargarArchivoPreprocesado(sys.argv[2])

        listaClusters=FileHandler.cargarObjeto(sys.argv[3])


        #Genero la lista de correlación de los clusters K-means

        resultado=""
        for i in range(0,20):


            resultado+="\n \n Iteración "+str(i)+":\n"
            listaKmeans = []
            #kmeans = K_Means.K_Means(X, 70)
            #listaClusters, clusters= kmeans.k_means()
            for i in range(0,70):
                indices = AnalyzeResults.obtenerIndicesIntancias(i, listaClusters)
                dicTags = AnalyzeResults.obtenerTagsVector(tags, indices)
                matrizTags = AnalyzeResults.matrizTagsIntanciasCluster(dicTags,True)
                matriz=AnalyzeResults.coeficientePearson(matrizTags)
                listaKmeans.append(np.nanmean(matriz))

            media=mean(listaKmeans)
            print(mean(listaKmeans))
            resultado+="Media KMeans "+str(media)+":\n"

            # Genero la lista de correlación del cluster aleatorio KMeans
            clusterAleatorio = ClusterAleatorio.ClusterAleatorio(X, 70)
            listaClustersAleatorio = clusterAleatorio.generarClusters()
            listaAleatorio = []
            matrizGeneral=np.array
            for i in range(0,70):
                indices = AnalyzeResults.obtenerIndicesIntancias(i, listaClustersAleatorio)
                dicTags = AnalyzeResults.obtenerTagsVector(tags, indices)
                matrizTags = AnalyzeResults.matrizTagsIntanciasCluster(dicTags,True)
                matriz=AnalyzeResults.coeficientePearson(matrizTags)
                listaAleatorio.append(np.nanmean(matriz))
            media2=mean(listaAleatorio)
            print(mean(listaAleatorio))
            # Genero la lista de correlación de los clusters aleatorios
            resultado+="Media KMeans aleatorio"+str(media2)+":\n"

            # Genero la lista de correlación del cluster completamente aleatorio
            listaClustersAleatorio2=Clusters.generarClusterAleatorio2(X,listaClusters)

            listaAleatorio2 = []
            matrizGeneral = np.array
            for i in range(0, 70):
                indices = AnalyzeResults.obtenerIndicesIntancias(i, listaClustersAleatorio2)
                dicTags = AnalyzeResults.obtenerTagsVector(tags, indices)
                matrizTags = AnalyzeResults.matrizTagsIntanciasCluster(dicTags,True)
                matriz = AnalyzeResults.coeficientePearson(matrizTags)
                listaAleatorio2.append(np.nanmean(matriz))
            media3=mean(listaAleatorio2)
            print(mean(listaAleatorio2))
            resultado+="Media aleatorio"+str(media3)+":\n"

        FileHandler.guardarDocumento(resultado,sys.argv[4]+"/recuento")
        print(resultado)
        Visualizacion.crearGraficoBarras(list(range(0,max(listaClusters)+1)),listaKmeans,"K-Means","Número de cluster","Correlación",0,75,5,True,sys.argv[4]+"/graficoCorrelacionKMeans")

        Visualizacion.crearGraficoBarras(list(range(0,max(listaClusters)+1)), listaAleatorio, "K-Means Aleatorio", "Número de cluster", "Correlación", 0,
                                      71, 5, True, sys.argv[4]+"/graficoCorrelacionKMeansAleatorio2")

        Visualizacion.crearGraficoBarras(list(range(0,max(listaClusters)+1)), listaAleatorio2, "Aleatorio", "Número de cluster",
                                          "Correlación", 0,71, 5, True, sys.argv[4]+"/graficoCorrelacionAleatorio")
