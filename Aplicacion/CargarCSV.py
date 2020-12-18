import sys
sys.path.append("..")
from Modelo import FileHandler,FilterData

if __name__=="__main__":

    if (len(sys.argv) - 1 != 7):
        print("Realiza el preprocesado de los documentos y etiquetas contenidos en un CSV. Genera dos archivos txt: \n"
              "- Un archivo que contiene un documento por línea formado por las palabras del documento separadas por comas"
              "- Un archivo con las etiquetas de cada documento en cada línea separadas por comas")
        print("El ejecutable tiene que ser llamado con siete argumentos: ")
        print("Ha sido llamado con: " +str(len(sys.argv)-1))
        print("Argumento 1: path del archivo csv")
        print("Argumento 2: columna en la que se encuentra el texto")
        print("Argumento 3: columna en la que se encuentran las etiquetas")
        print("Argumento 4: T si se quiere aplicar el Stemmer F en caso contrario")
        print("Argumento 5: T si se quiere aplicar el Lemmatizer F en caso contrario")
        print("Argumento 6: T si se quiere aplicar el StopWords F en caso contrario")
        print("Argumento 7: Carpeta en la que se van a almacenar los archivos generados")

    else:
        print("Ejecutable llamado correctamente")

        for i in sys.argv:
            print(i)

        doc, tags = FileHandler.cargarCSV(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

        stem= False
        lema=False
        stop=False
        if (sys.argv[4] == "T"):
            print("Se aplicara stemmer")
            stem = True
        if (sys.argv[5] == "T"):
            print("Se aplicara lemmatizer")
            lema = True
        if (sys.argv[5] == "T"):
            print("Se aplicara stop words")
            stop = True
        doc2 = FilterData.preprocesado(doc, stem, lema, stop)

        pathEtiquetas = FileHandler.anadirSubstringPath( FileHandler.quitarExtension(sys.argv[1].split('/')[-1])+ '_tags_decoded.txt', sys.argv[7])

        pathDocumentos = FileHandler.anadirSubstringPath(FileHandler.quitarExtension(sys.argv[1].split('/')[-1]) + '_decoded.txt', sys.argv[7])


        FileHandler.guardarDocumento(tags,pathEtiquetas)
        FileHandler.guardarDocumento(doc2,pathDocumentos)

        print("Generado el archivo: " + pathEtiquetas)
        print("Generado el archivo: " + pathDocumentos)
