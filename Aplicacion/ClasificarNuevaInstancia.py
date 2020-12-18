import operator
import sys
import numpy as np
sys.path.append("..")

from Modelo import FileHandler, Transform, FilterData, K_Means, AnalyzeResults, Distancias

if __name__ == "__main__":

    if (len(sys.argv)-1!=8):
        print("Ejecutable que localiza el cluster al que pertenece una instancia y devuelve las cercanas a esta")
        print("El ejecutable tiene que ser llamado con ocho argumentos: ")
        print("Ha sido llamado con: " + str(len(sys.argv) - 1))
        print("Argumento 1: documento a situar en el cluster")
        print("Argumento 2: modelo LDA generado con los documentos de entrenamiento")
        print("Argumento 3: lista de centroides obtenida al aplicar el K_Means sobre los datos de entrenamiento")
        print("Argumento 4: lista de pertenencia de instancias a los clusters")
        print("Argumento 5: lista de vectores de topicos")
        print("Argumento 6: csv con documentos de entrenamiento")
        print("Argumento 7: cantidad de documentos cercanos que se quieren almacenar")
        print("Argumento 8: path completo (carpeta y nombre) en el que almacenar los documentos más cercanos a la instancia")

    else:
        documento=FileHandler.cargarArchivo(sys.argv[1])

        modelo=FileHandler.cargarModeloLDA(sys.argv[2])

        centroides=FileHandler.cargarObjeto(sys.argv[3])

        listaClusters=FileHandler.cargarObjeto(sys.argv[4])

        vectoresEntrenamiento=FileHandler.cargarObjeto(sys.argv[5])

        documentos,etiqueta=FileHandler.cargarCSV(sys.argv[6],2,3)

        documentos=documentos.split("\n")

        #Se realiza el preprocesado del documento:
        documento=FilterData.preprocesadoDocumento(documento,True,True,True)

        #Se obtiene el vector de tópicos partiendo del modelo LDA de entrenamiento
        vectorTopics=Transform.obtenerVectorTopics(modelo,documento)
        dicTopics=zip(vectorTopics,range(0,50))
        dicTopics=sorted(dict(dicTopics).items(),reverse=True)
        dicTopics=dict(dicTopics)

        print("Los diez topics más relevantes de la instancia son: "+str(list(dicTopics.values())[:10]))

        #Se emplea el método escogerCentroide del K_means para elegir el centroide óptimo
        kmeans=K_Means.K_Means(vectorTopics,40,"euclidea")
        centroideCercano,indiceCentroide,distancias=kmeans.escogerCentroide(np.array(vectorTopics),np.array(centroides))


        print("El cluster más cercano a la instancia es el número: "+str(indiceCentroide))
        #Se obtienen los documentos de las  N instancias más cercanas al documento y se almacenan en el path indicado
        indices=AnalyzeResults.obtenerIndicesIntancias(indiceCentroide,listaClusters)
        dicCercanas=AnalyzeResults.obtenerTopicsInstancias(vectoresEntrenamiento,indices)

        diccionarioIndicesCercanos={}

        for key in dicCercanas:
            vectorActual=dicCercanas[key]
            distancia=Distancias.distanciaEuclidea(vectorActual,vectorTopics)
            diccionarioIndicesCercanos[key]=distancia

        listaTuplasIndicesCercanos=sorted(diccionarioIndicesCercanos.items(), key=operator.itemgetter(1), reverse=False)

        resultado="El cluster más cercano a la instancia es el número: "+str(indiceCentroide)+"\n"
        for i in range(0,int(sys.argv[7])):
            indice=listaTuplasIndicesCercanos[i][0]
            distancia=listaTuplasIndicesCercanos[i][1]
            resultado+="Documento "+indice+" distancia="+str(distancia)+"\n"+str(documentos[int(indice)])+"\n"

        FileHandler.guardarDocumento(resultado,sys.argv[8])
