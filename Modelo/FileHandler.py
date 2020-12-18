import csv
import pickle
import tomotopy as tp

def cargarCSV(path,colText,colTags):
    """ Carga el archivo csv almacenando las etiquetas en un String y los documentos en otro
                   Parámetros:
                       path -- path en el que se encuentra el csv
                       colText -- columna del csv en la que se encuentran los documentos
                       colTags -- columna del csv en la que se encuentran las etiquetas
    """
    with open(path, newline='') as File:
        reader = csv.reader(File)
        allDocs=''
        allTags=''
        i=0
        for row in reader:
            if(i!=0):
                text=row[colText]+'\n'
                allDocs=allDocs+text
                tags=row[colTags]+'\n'
                tags=tags.replace(';',',')
                allTags=allTags+tags
            i=i+1
    File.close()

    return allDocs,allTags

def ndarrayToString(predicciones):
    """ Recibe las predicciones en formato ndarray y las convierte en String

                 Parámetros:
                        predicciónes -- matriz ndarray con las predicciones
    """
    x=predicciones.shape[0]

    y=predicciones.shape[1]

    pred=""
    for i in range(0,x):
        fila=""

        for j in range(0,y):
            num=predicciones[i,j]
            fila=fila+str(num)+","
        fila=fila.rstrip(',')

        pred=pred+fila+"\n"

    return pred

def guardarDocumento(text,path):
    """ Guarda el texto text en el documento indicado en el path
                   Parámetros:
                       text -- texto a almacenar
                       path -- path en el que almacenar el texto
        """
    f4 = open(path, 'a')
    f4.write(text)
    f4.write("\n")
    f4.close()


def quitarExtension(nombre):
    """ Quita la extensión a un nombre
                   Parámetros:
                       nombre -- nombre al que quitar la extensión
    """
    nombre=nombre.split('.')
    return nombre[0]

def anadirSubstringPath(nombre, carpeta):
    """ Añade un documento de nombre nombre en la carpeta indicada
                   Parámetros:
                       nombre -- nombre del documento
                       carpeta -- path de la carpeta en la que se va a almacenar el documento
        """
    return carpeta+'/'+nombre


def cargarArchivoPreprocesado(filePath):
    """ Carga un archivo de un path y lo convierte en una lista de listas donde en cada lista se almacenan las etiquetas
        o palabras de un documento
            Parámetros:
                filePath -- path del archivo a cargar
    """
    f = open(filePath)
    corpus = []
    i=0
    for document in f:
        document = document.replace("\n", "")
        document = document.split(',')
        corpus.append(document)
        i=i+1

    f.close()
    return corpus


def obtenerListaParametros(strParam):
    """ Dado un string separado por comas, devuelve sus elementos en una lista de números
                   Parámetros:
                       strParam -- String que contiene los parámetros separados por comas
    """
    lista=[]
    param=strParam.split(',')

    for i in param:
        if "." in i:
            num=float(i)
        else:
            num=int(i)
        lista.append(num)
    return lista


def guardarObjeto(matrizTrain, path):
    """ Guarda el objeto en el path indicado
                    Parámetros:
                        matrizTrain --  objeto
                        path -- path en el que almacenar el objeto
        """
    with open(path, "wb") as f:
        pickle.dump(matrizTrain, f)


def cargarObjeto(path):
    """ Carga el objeto del path indicado
                        Parámetros:
                            path -- path del que cargar el objeto
            """
    with open(path, "rb") as f:
        obj = pickle.load(f)
    return obj

def cargarArchivoPreprocesadoEnLista(filePath):
    """ Carga un archivo de un path y lo convierte en una lista donde en cada lista se almacena un string con las etiquetas
            o palabras de un documento
                Parámetros:
                    filePath -- path del archivo a cargar
        """
    f = open(filePath)
    corpus = []
    i = 0
    for document in f:
        document = document.replace("\n", "")
        document = document.split(',')
        for palabra in document:
            corpus.append(palabra)
        i = i + 1

    f.close()
    return corpus

def cargarModeloLDA(path):
    """ Carga el modelo LDA del path indicado
                   Parámetros:
                       path -- path del que cargar el modelo
        """
    model = tp.LDAModel.load(path)
    return model

def guardarModelo(modelo,path):
    """ Guarda el modelo PLDA o LLDA en el path indicado
               Parámetros:
                   modelo -- modelo PLDA o LLDA de la librería Tomotopy
                   path -- path en el que almacenar el modelo
    """
    modelo.save(path)

def cargarArchivo(path):
    """ Carga un archivo del path indicado
                       Parámetros:
                           path -- path del que cargar el archivo
            """
    f=open(path)
    string=""
    for linea in f:
        string+=linea
    f.close()
    return string
