import sys

sys.path.append("..")

from Modelo import FileHandler

if __name__ == "__main__":

    if __name__ == "__main__":
        if (len(sys.argv) - 1 != 3):
            print("Ejecutable que obtiene las n palabras más relevantes de los tópicos las almacena en un documento \n"
                  "donde en cada línea se guardan las palabras del íésimo topic junto con su relevancia")
            print("El ejecutable tiene que ser llamado con tres argumentos:")
            print("Ha sido llamado con: " + str(len(sys.argv) - 1))
            print("Argumento 1: modelo LDA")
            print("Argumento 2: cantidad de palabras a obtener")
            print("Argumento 3: path en el que almacenar el documento")

        else:
            modelo=FileHandler.cargarModeloLDA(sys.argv[1])
            vectorPal=""
            for i in range(0, modelo.k):
                vectorPal = vectorPal + str(modelo.get_topic_words(i, top_n=int(sys.argv[2]))) + "\n"
            FileHandler.guardarDocumento(str(vectorPal), sys.argv[3])