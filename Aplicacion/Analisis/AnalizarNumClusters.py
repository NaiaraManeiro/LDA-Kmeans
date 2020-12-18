import sys

import numpy


sys.path.append("../..")
from Modelo import FileHandler, Clusters,Visualizacion

if __name__ == "__main__":

    if (len(sys.argv) - 1 != 5):
        print("Ejecutable para elegir la cantidad óptima de clusters a generar. Realiza un barrido del parámetro K "
            "variando el valor en el rango indicado en los parámetros. Genera un archivo con los resultados cada 10 iteraciones. Además genera los gráficos"
              "correspondientes a la evolución de las métricas BSS y SSE \n")
        print("El ejecutable tiene que ser llamado con cuatro argumentos:")
        print("Ha sido llamado con: " + str(len(sys.argv) - 1))
        print("Argumento 1: path del conjunto de datos ")
        print("Argumento 2: valor en el que empezar las iteraciones, cada cuanto saltar, valor final separados por comas:"
              "por ejemplo 10,50,10, generaría los resultados de crear 10-20-30-40-50 clusters")
        print("Argumento 3: directorio en el que almacenar los resultados")
        print("Argumento 4: T si se quieren guardar los gráficos F en caso contrario (solo se mostrarán)")
        print("Argumento 5: indicar la distancia (euclidea o manhattan) para realizar los cálculos del K-Means")


    else:

        X= FileHandler.cargarObjeto(sys.argv[1])

        listaParam=FileHandler.obtenerListaParametros(sys.argv[2])

        numClusters,resultadosSSE,resultadosBSS=Clusters.newNumCluster(numpy.array(X),listaParam[0],listaParam[1]+10,listaParam[2],True,sys.argv[3],sys.argv[5])

        guardar=False
        if(sys.argv[4]=="T"):
            guardar=True+listaParam
        #Crear gráficos de barras
        saltoGráfico=(listaParam[0]+listaParam[2])/10
        Visualizacion.crearGraficoBarras(numClusters, resultadosSSE, "Evolución SSE", "Cantidad de clusters", "SSE", listaParam[0],listaParam[1]+10,saltoGráfico,guardar,
                                         sys.argv[3]+"/graficoSSE")
        Visualizacion.crearGraficoBarras(numClusters,resultadosBSS,"Evolución BSS","Cantidad de clusters","BSS",listaParam[0],listaParam[1]+10,listaParam[2],guardar,
                                         sys.argv[3]+"/graficoBSS")



