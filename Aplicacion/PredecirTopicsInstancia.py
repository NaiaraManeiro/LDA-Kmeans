import sys
sys.path.append("..")


from Modelo import FileHandler, FilterData, Transform


if __name__ == "__main__":
    if (len(sys.argv) - 1 != 3):
        print("Ejecutable que genera el vector de topicos de un documento partiendo de un modelo LDA")
        print("El ejecutable tiene que ser llamado con tres argumentos: ")
        print("Ha sido llamado con: " + str(len(sys.argv) - 1))
        print("Argumento 1: path del archivo txt con el documento")
        print("Argumento 2: path del modelo")
        print("Argumento 3: path en el que almacenar el vector")

    else:

        modeloLDA=FileHandler.cargarModeloLDA(sys.argv[2])

        documento=FileHandler.cargarArchivoPreprocesado(sys.argv[1])

        documentoPreprocesado=FilterData.preprocesado(documento,True,True,True)
        print(documentoPreprocesado)

        vector=Transform.obtenerVectorTopics(modeloLDA,documentoPreprocesado)

        FileHandler.guardarObjeto(vector,sys.argv[3]+"objeto")

        FileHandler.guardarDocumento(str(vector), sys.argv[3])