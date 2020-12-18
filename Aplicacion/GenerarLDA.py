import sys

sys.path.append("..")

from Modelo import Transform,FileHandler


if __name__ == "__main__":
    if (len(sys.argv) - 1 != 4):
        print("Ejecutable que genera el modelo LDA partiendo de los documentos")
        print("El ejecutable tiene que ser llamado con cuatro argumentos: ")
        print("Ha sido llamado con: " + str(len(sys.argv) - 1))
        print("Argumento 1: path del archivo txt preprocesado con todos los documentos")
        print("Argumento 2: valor de los parámetros seguidos por comas en el orden: \n"
              "             min_cf,min_df,rm_top,k,alpha,eta\n"
              "             Por ejemplo: 10,0,0,1,0.2,0.1")
        print("Argumento 3: Path en el que almacenar el modelo")
        print("Argumento 4: Path en el que almacenar los topics vectors")
    else:
        documentos=FileHandler.cargarArchivoPreprocesado(sys.argv[1])
        parametros=FileHandler.obtenerListaParametros(sys.argv[2])
        print(parametros)

        min_cf = parametros[0]
        min_df = parametros[1]
        rm_top = parametros[2]
        k = parametros[3]
        alpha = parametros[4]
        eta = parametros[5]
        vector,modelo=Transform.LDA(min_df,min_cf,rm_top,k,alpha,eta,documentos)
        print(type(vector[0]))
        FileHandler.guardarModelo(modelo,sys.argv[3])

        FileHandler.guardarDocumento(str(vector),sys.argv[4])
        FileHandler.guardarObjeto(vector,sys.argv[4]+"objeto")
        vectorPal=""
        for i in range(0,50):
            vectorPal=vectorPal+str(modelo.get_topic_words(i, top_n=10))+"\n"
        FileHandler.guardarDocumento(str(vectorPal), sys.argv[3]+"palabras")