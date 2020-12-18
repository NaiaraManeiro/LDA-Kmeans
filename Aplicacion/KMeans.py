import sys
sys.path.append("..")

from Modelo import FileHandler, Clusters, K_Means

if __name__ == "__main__":
    if (len(sys.argv) - 1 !=4):
        print("Ejecutable que calcula el cluster K-Means")
        print("El ejecutable tiene que ser llamado con cuatro argumentos: ")
        print("Ha sido llamado con: " + str(len(sys.argv) - 1))
        print("Argumento 1: path al conjunto de datos (objeto que contiene los vectores LDA)")
        print("Argumento 2: cantidad de clusters que se quieren crear")
        print("Argumento 3: directorio en el que almacenar los resultados")
        print("Argumento 4: indicar la distancia (euclidea o manhattan) para realizar los cálculos del K-Means")
    else:
        X = FileHandler.cargarObjeto(sys.argv[1])

        kmeans=K_Means.K_Means(X,70,sys.argv[4])

        listaClusters,centroides=kmeans.k_means()

        strResultado=""
        for i in listaClusters:
            vector=X[i]
            strResultado+="Cluster número "+str(i)+"   Vector de la instancia:  "+str(vector)+"\n\n"

        FileHandler.guardarDocumento(strResultado,sys.argv[3]+"/asignacionInstancias")

        FileHandler.guardarObjeto(listaClusters,sys.argv[3]+"/listaClusters")
        FileHandler.guardarObjeto(centroides,sys.argv[3]+"/centroides")


        print("Coordenadas de los centroides ")

        for centroide in centroides:
            print(centroide)
            print("\n")
        print("\n\n")
        sse=Clusters.SSE(X,listaClusters,centroides)
        bss = Clusters.BSS(listaClusters,X,centroides)

        print("Indicadores de la calidad del clustering: \n")
        print("SSE="+str(sse))
        print("BSS="+str(bss))