import operator
import sys

import numpy as np

sys.path.append("../..")

from Modelo import FileHandler, Visualizacion, AnalyzeResults, AnalyzeCorpus

if __name__ == "__main__":

    if (len(sys.argv) - 1 != 7):
        print("Ejecutable que realiza un analisis de las etiquetas y de los topicos principales del cluster indicado \n"
              "Genera graficos con la frecuencia de las etiquetas y las nubes de palabras de los topics principales")
        print("El ejecutable tiene que ser llamado con siete argumentos:")
        print("Ha sido llamado con: " + str(len(sys.argv) - 1))

        print("Argumento 1: path al conjunto de documentos preprocesado ")
        print("Argumento 2: path al conjunto de etiquetas")
        print("Argumento 3: vector LDA")
        print("Argumento 4: lista de los clusters")
        print("Argumento 5: modelo LDA")
        print("Argumento 6: indice del cluster a analizar")
        print("Argumento 7: path en el que almacenar los graficos generados")

    else:

        documentos = FileHandler.cargarArchivoPreprocesado(sys.argv[1])
        etiquetas = FileHandler.cargarArchivoPreprocesado(sys.argv[2])

        vectores = FileHandler.cargarObjeto(sys.argv[3])

        listaClusters = FileHandler.cargarObjeto(sys.argv[4])
        print(sys.argv[6])
        indices=AnalyzeResults.obtenerIndicesIntancias(int(sys.argv[6]),listaClusters)

        #Se obtienen las etiquetas de mayor aparicion en el cluster y se crea un gráfico de barras con las frecuencias
        setEtiquetas=set()
        dicApEtDoc={}
        listaEtiquetas=[]
        for i in indices:
            etiquetasInstancia=etiquetas[i]
            for etiqueta in etiquetasInstancia:
                setEtiquetas.add(etiqueta)
                listaEtiquetas.append(etiqueta)
                if etiqueta not in dicApEtDoc.keys():
                    dicApEtDoc[etiqueta]=1
                else:
                    dicApEtDoc[etiqueta]=dicApEtDoc[etiqueta]+1

        recuento=AnalyzeCorpus.obtenerRecuento(listaEtiquetas)
        recuento=dict(recuento)
        recuento=dict(sorted(recuento.items(), key=operator.itemgetter(1), reverse=True))
        my_list = list(recuento.values())

        ejeY = list(map(lambda x: (x / len(indices)) * 100, my_list))

        Visualizacion.crearGraficoBarras(list(recuento.keys()),ejeY,"Frecuencia de etiquetas en los documentos","Etiqueta","Porcentaje de documentos",0,0,0,True,sys.argv[7]+"/FreqEtiquetas")


        #Se obtienen los grupos de etiquetas de mayor aparición en el cluster y se crea un gráfico de barras con las frecuencias
        dic={}
        for i in indices:
            etiquetasInstancia=etiquetas[i]
            setTipo=set()
            for etiqueta in etiquetasInstancia:
                tipo=etiqueta.split(".")[0]
                setEtiquetas.add(tipo)
                listaEtiquetas.append(tipo)
                if tipo not in setTipo:
                    setTipo.add(tipo)
                    if tipo not in dic.keys():
                        dic[tipo]=1
                    else:
                        dic[tipo]=dic[tipo]+1

        recuento=dict(sorted(dic.items(), key=operator.itemgetter(1), reverse=True))
        my_list = list(recuento.values())

        ejeY=list(map(lambda x: (x / len(indices))*100, my_list))

        Visualizacion.crearGraficoBarras(list(recuento.keys()),ejeY,"Frecuencia de tipos de etiquetas en los documentos","Etiqueta","Porcentaje de documentos",0,0,0,True,sys.argv[7]+"/FreqTipoEtiquetas")


        #Se obtienen los 5 topics más relevantes del cluster para ello se suman las frecuencias de los topics de todos los vectores y se eligen los 5
        # de mayor frecuencia
        print("Las instancias del cluster "+sys.argv[6] +" son "+str(indices))
        listaRango=list(range(0,50))
        matriz = []
        for i in indices:
            matriz.append(vectores[i])
        vectorRec=np.apply_along_axis(sum, 0, matriz)
        listaVector=vectorRec.tolist()
        dic=dict(zip(listaRango,listaVector))
        ordenados=sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
        indices=[]
        for i in range(0,5):
            indices.append(ordenados[i][0])

        modeloLDA=FileHandler.cargarModeloLDA(sys.argv[5])
        for i in indices:
            palabras=modeloLDA.get_topic_words(i,top_n=15)
            Visualizacion.crearGraficodePalabras(dict(palabras),True,sys.argv[7]+"/pruebaPalTopics"+str(i))