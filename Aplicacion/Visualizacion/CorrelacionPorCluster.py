import sys
sys.path.append("../..")

from Modelo import FileHandler, AnalyzeResults, Visualizacion

if __name__ == "__main__":

    if (len(sys.argv)-1!=2):
        print("Ejecutable que analiza la distribución de palabras de los documentos calcula la media, mediana, moda, varianza \n"
              ",desviación típica y el máximo y mínimo de palabras que puede contener un documento")
        print("El ejecutable tiene que ser llamado con dos argumentos: ")
        print("Ha sido llamado con: " + str(len(sys.argv) - 1))
        print("Argumento 1: path del archivo que contiene la lista de clusters")
        print("Argumento 2: path del archivo que contiene las etiquetas de todos los documentos")
    else:

        for i in range(0,70):
            listaClusters = FileHandler.cargarObjeto(sys.argv[1])
            tags = FileHandler.cargarArchivoPreprocesado(sys.argv[2])
            indices = AnalyzeResults.obtenerIndicesIntancias(i, listaClusters)
            dicTags = AnalyzeResults.obtenerTagsVector(tags, indices)

            #Para comparar cuando las etiquetas son exactamente iguales
            matrizTags1 = AnalyzeResults.matrizTagsIntanciasCluster(dicTags, True)
            corr1 = AnalyzeResults.coeficientePearson(matrizTags1)

            Visualizacion.heatmap(corr1, "HeatMap de la matriz de correlación para el Cluster" + str(i) + "", True,
                                  "../../Archivos/Correlacion/HeatMaps/heatMapCluster" + str(i) + "")

            #Para comparar cuando las etiquetas son iguales delante del punto
            matrizTags2 = AnalyzeResults.matrizTagsIntanciasCluster(dicTags, False)
            corr2 = AnalyzeResults.coeficientePearson(matrizTags2)

            Visualizacion.heatmap(corr2, "HeatMap de la matriz de correlación para el Cluster" + str(i) + "", True,
                                  "../../Archivos/Correlacion/HeatMaps1/heatMapCluster" + str(i) + "")

            # Para comparar cuando las etiquetas están dentro de un rango
            matrizTags3 = AnalyzeResults.matrizTagsRangoIntanciasCluster(dicTags)
            corr3 = AnalyzeResults.coeficientePearson(matrizTags3)

            Visualizacion.heatmap(corr3, "HeatMap de la matriz de correlación para el Cluster" + str(i) + "", True,
                                 "../../Archivos/Correlacion/HeatMaps2/heatMapCluster" + str(i) + "")