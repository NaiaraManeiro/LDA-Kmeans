import sys
sys.path.append("..")


from Modelo import FileHandler, Clusters, Visualizacion

if __name__ == "__main__":
    if len(sys.argv) - 1 != 5:
        print("Ejecutable que repite un cluster el número de veces indicado y elige el mejor")
        print("El ejecutable tiene que ser llamado con cuatro argumentos: ")
        print("Ha sido llamado con: " + str(len(sys.argv) - 1))
        print("Argumento 1: path al conjunto de datos")
        print("Argumento 2: cantidad de clusters que se quieren crear")
        print("Argumento 3: cantidad de iteraciones")
        print("Argumento 4: directorio en el que almacenar los objetos")
        print("Argumento 5: indicar la distancia (euclidea o manhattan) para realizar los cálculos del K-Means")

    else:

        X = FileHandler.cargarObjeto(sys.argv[1])

        numClusters=sys.argv[2]

        numIteraciones=sys.argv[3]

        listaIter=list(range(1,int(numIteraciones)+1))

        path = sys.argv[4]

        listaClusters, clusters,listaBSS,listaSSE=Clusters.generarClusterOptimo(X,int(numIteraciones),int(numClusters),sys.argv[5])

        FileHandler.guardarObjeto(listaClusters,path+"/listaClusters")
        FileHandler.guardarObjeto(clusters,path+"/clusters")

        Visualizacion.graficoPuntoRaya(listaIter, listaSSE, "Evolución SSE", "Cantidad de clusters", "SSE", 0,
                                         int(numIteraciones) + 1, 1, True,
                                         path + "/graficoSSE")

        Visualizacion.graficoPuntoRaya(listaIter, listaBSS, "Evolución BSS", "Cantidad de clusters", "BSS", 0,
                                         int(numIteraciones) + 1, 1, True,
                                         path + "/graficoBSS")

        # Visualizacion.crearGraficoBarras(listaIter,listaSSE, "Evolución SSE", "Cantidad de clusters", "SSE", 0,int(numIteraciones)+1,1,True,
        #                                  path+"/graficoSSE")
        #
        # Visualizacion.crearGraficoBarras(listaIter, listaBSS, "Evolución BSS", "Cantidad de clusters", "BSS", 0,int(numIteraciones)+1,1, True,
        #                                  path + "/graficoBSS")
        #Valores cluster óptimo: BSS977.6615913124949
                                #SSE685.9251197431296

