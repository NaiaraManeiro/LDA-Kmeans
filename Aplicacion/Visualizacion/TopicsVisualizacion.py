
import sys
sys.path.append("../..")

from Modelo import FileHandler, Visualizacion
from collections import Counter

if __name__ == "__main__":
    if (len(sys.argv)-1!=1):
        print("Ejecutable que crea nubes de 10 palabras de los topics")
        print("El ejecutable tiene que ser llamado con un argumento: ")
        print("Ha sido llamado con: " + str(len(sys.argv) - 1))
        print("Argumento 1: path del archivo que contiene los topics")
    else:
        palabrasTopics = FileHandler.cargarArchivoPreprocesado(sys.argv[1])

        listaFinal = []
        listaPatologias = []
        for i in range(0, len(palabrasTopics)):
            topics = {}
            listaTopics = []
            lista = palabrasTopics[i]
            j = 0
            while j < 20:
                pat = lista[j]
                pat = pat.replace("[('", "")
                pat = pat.replace(" (", "")
                patologia = pat.replace("'", "")
                val = lista[j+1]
                val = val.replace(" ", "")
                val = val.replace("]", "")
                valor = val.replace(")", "")
                #Matriz sin caracteres raros
                listaTopics.append((patologia, valor))
                # Para el counter
                listaPatologias.append(patologia)
                # Diccionario {topic: propabilidad}
                topics[str(patologia)] = float(valor)
                j += 2
            listaFinal.append(listaTopics)
            Visualizacion.crearGraficodePalabras(topics, False, "../Archivos/NubesPalabras/palabrasTopic" + str(i) + "")

        counter = Counter(listaPatologias)

        datos = []

        for i in range(0, len(listaFinal)):
            listaTopics = []
            lista = listaFinal[i]
            j = 0
            while j < 10:
                patologia = lista[j][0]
                valor = lista[j][1]
                listaTopics.append([patologia, i, float(valor), counter[patologia]])
                j += 1
            datos.append(listaTopics)
        for i in range(0, 3):
            Visualizacion.graficoBarrasNubePalabras(datos[i])
