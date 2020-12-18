import sys
import numpy as np

sys.path.append("..")

from Modelo import FileHandler, Visualizacion, AnalyzeResults, Distancias

if __name__ == "__main__":
    if (len(sys.argv) - 1 != 4):
        print("Ejecutable que calcula la distancia Jensen Shannon entre los vectores de los clusters \n"
              "Genera mapas de calor con la distancia entre las instancias de los clusters")
        print("El ejecutable tiene que ser llamado con cuatro argumentos:")
        print("Ha sido llamado con: " + str(len(sys.argv) - 1))
        print("Argumento 1: vectores LDA del conjunto")
        print("Argumento 2: etiquetas del conjunto")
        print("Argumento 3: lista de los clusters")
        print("Argumento 4: directorio en el que almacenar los HeatMaps")

    else:

        X = FileHandler.cargarObjeto(sys.argv[1])
        tags = FileHandler.cargarArchivoPreprocesado(sys.argv[2])

        listaClusters=FileHandler.cargarObjeto(sys.argv[3])

        #Se calcula la distancia entre todas las instancias de cada cluster y se crea una matriz para generar el heatMap
        media=0
        minimo=10000000
        for k in range(0, 70):
            indices = AnalyzeResults.obtenerIndicesIntancias(k, listaClusters)
            dicVectores = AnalyzeResults.obtenerTopicsInstancias(X, indices)
            matriz = []
            for i in indices:
                vector1 = dicVectores[str(i)]
                fila = []
                for j in indices:
                    vector2 = dicVectores[str(j)]
                    distanciaJensen = Distancias.jensenShannonDistance(vector1, vector2)
                    fila.append(distanciaJensen)
                matriz.append(fila)
            media+=np.mean(np.array(matriz))
            mediaAct=np.mean(np.array(matriz))
            if(mediaAct<minimo):
                minimo=mediaAct
                clusterMin=k
            Visualizacion.heatmap(np.array(matriz),"Matriz distancia Jensen Shannon",True,sys.argv[4]+"/heatMapCluster"+str(k))

        print("La media de la distancia Jensen Shannon del clustering es: "+str(media/70))
        print("El cluster de menor distancia Jensen Shannon es: "+str(clusterMin)+" El valor para esta distancia es: "+ print(str(clusterMin)))
