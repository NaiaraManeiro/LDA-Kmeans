import math


from Modelo import FileHandler
import numpy as np

def obtenerIndicesIntancias(cluster, listaClusters):
    """ Obtenemos los índices de las instancias que pertenecen al cluster dado por parámetro
                        Parámetros:
                            cluster -- el número de cluster
                            listaClusters -- lista de que instancias pertenecen a que cluster
                    """
    indices = []
    i = 0
    for instancia in listaClusters:
        if instancia == cluster:
            indices.append(i)
        i+=1
    return indices

def obtenerTagsVector(vector, indices):
    """ Obtenemos las etiquetas correspondientes a los índices de instancias dados
                        Parámetros:
                            vector -- vector de etiquetas
                            indices -- inidices de instancias
                    """
    dicTags = {}
    for i in indices:
        if(i==8058):
            i=8057
        tag = vector[i]
        dicTags[str(i)] = tag

    return dicTags

def obtenerPalabrasVector(vector, indices):
    """ Obtenemos las palabras correspondientes a los índices de instancias dados
                        Parámetros:
                            vector -- vector de palabras
                            indices -- inidices de instancias
                    """
    dicPalabras = {}
    for i in indices:
        palabras = vector[i]
        dicPalabras[str(i)] = palabras
    return dicPalabras

def obtenerTopicsInstancias(matriz, indices):
    """ Obtenemos un diccionario con los vectores de tópicos correspondientes a los índices de instancias dados
                           Parámetros:
                               matriz -- matriz que contiene los vectores por filas
                               indices -- inidices de instancias
                       """
    dic={}

    for indice in indices:
        dic[str(indice)]=matriz[indice]

    return dic

def obtenerTags():
    """ Devuelve una lista de los 50 tags existentes
            """
    tags = FileHandler.cargarArchivoPreprocesado("../../Archivos/train_50_tags_decoded.txt")
    lista = []
    for tag in tags:
        for i in tag:
            if not i in lista:
                lista.append(i)
    return lista

def matrizTagsIntanciasCluster(dicTags, tagEntero):
    """ Calcula una matriz One-Hot-Encoding de 1s y 0s según la igualdad de las etiquetas del dicionario
        con todas las etiquetas existentes.
                        Parámetros:
                            dicTags -- diccionario de etiquetas de x instancias
                            tagEntero -- boolean para saber si hay que comparar las etiquetas en
                                        su totalidad o no
            """

    tags = obtenerTags()
    dicMatriz = {}

    for key in dicTags:
        listaTags01 = []
        tagDic = dicTags[key]
        lleno = False
        for i in tagDic:
            if not tagEntero:
                i = str(i).split(".")[0]
            cont = 0
            for tag in tags:
                if not tagEntero:
                    tag = str(tag).split(".")[0]
                if not lleno:
                    if i == tag:
                        listaTags01.append(1)
                    else:
                        listaTags01.append(0)
                else:
                    if i == tag:
                        listaTags01[cont] = 1
                cont += 1
            lleno = True

        dicMatriz[str(key)] = listaTags01

    return dicMatriz

def matrizTagsRangoIntanciasCluster(dicTags):
    """ Calcula una matriz One-Hot-Encoding con números de 0 a 19 según la igualdad de las etiquetas del dicionario
            y todas las etiquetas existentes dentro de unos rangos.
                        Parámetros:
                            dicTags -- diccionario de etiquetas de x instancias
            """

    tags = obtenerTags()
    dicMatriz = {}

    for key in dicTags:
        listaTags01 = []
        tagDic = dicTags[key]
        lleno = False
        for i in tagDic:
            primeraLetraI = str(i)[0]
            if primeraLetraI != 'V' and primeraLetraI != 'E':
                i = float(i)
            cont = 0
            for tag in tags:
                primeraLetraTag = str(tag)[0]
                if primeraLetraTag != 'V' and primeraLetraTag != 'E':
                    tag = float(tag)
                if primeraLetraTag != 'V' and primeraLetraTag != 'E' and primeraLetraI != 'V' and primeraLetraI != 'E':
                    if not lleno:
                        if 1 < i < 139 and 1 < tag < 139:
                            listaTags01.append(1)
                        elif 140 < i < 239 and 140 < tag < 239:
                            listaTags01.append(2)
                        elif 240 < i < 279 and 240 < tag < 279:
                            listaTags01.append(3)
                        elif 280 < i < 289 and 280 < tag < 289:
                            listaTags01.append(4)
                        elif 290 < i < 319 and 290 < tag < 319:
                            listaTags01.append(5)
                        elif 320 < i < 389 and 320 < tag < 389:
                            listaTags01.append(6)
                        elif 390 < i < 459 and 390 < tag < 459:
                            listaTags01.append(7)
                        elif 460 < i < 519 and 460 < tag < 519:
                            listaTags01.append(8)
                        elif 520 < i < 579 and 520 < tag < 579:
                            listaTags01.append(9)
                        elif 580 < i < 629 and 580 < tag < 629:
                            listaTags01.append(10)
                        elif 630 < i < 679 and 630 < tag < 679:
                            listaTags01.append(11)
                        elif 680 < i < 709 and 680 < tag < 709:
                            listaTags01.append(12)
                        elif 710 < i < 739 and 710 < tag < 739:
                            listaTags01.append(13)
                        elif 740 < i < 759 and 740 < tag < 759:
                            listaTags01.append(14)
                        elif 760 < i < 779 and 760 < tag < 779:
                            listaTags01.append(15)
                        elif 780 < i < 799 and 780 < tag < 799:
                            listaTags01.append(16)
                        elif 800 < i < 999 and 800 < tag < 999:
                            listaTags01.append(17)
                        else:
                            listaTags01.append(0)
                    else:
                        if 1 < i < 139 and 1 < tag < 139:
                            listaTags01[cont] = 1
                        elif 140 < i < 239 and 140 < tag < 239:
                            listaTags01[cont] = 2
                        elif 240 < i < 279 and 240 < tag < 279:
                            listaTags01[cont] = 3
                        elif 280 < i < 289 and 280 < tag < 289:
                            listaTags01[cont] = 4
                        elif 290 < i < 319 and 290 < tag < 319:
                            listaTags01[cont] = 5
                        elif 320 < i < 389 and 320 < tag < 389:
                            listaTags01[cont] = 6
                        elif 390 < i < 459 and 390 < tag < 459:
                            listaTags01[cont] = 7
                        elif 460 < i < 519 and 460 < tag < 519:
                            listaTags01[cont] = 8
                        elif 520 < i < 579 and 520 < tag < 579:
                            listaTags01[cont] = 9
                        elif 580 < i < 629 and 580 < tag < 629:
                            listaTags01[cont] = 10
                        elif 630 < i < 679 and 630 < tag < 679:
                            listaTags01[cont] = 11
                        elif 680 < i < 709 and 680 < tag < 709:
                            listaTags01[cont] = 12
                        elif 710 < i < 739 and 710 < tag < 739:
                            listaTags01[cont] = 13
                        elif 740 < i < 759 and 740 < tag < 759:
                            listaTags01[cont] = 14
                        elif 760 < i < 779 and 760 < tag < 779:
                            listaTags01[cont] = 15
                        elif 780 < i < 799 and 780 < tag < 799:
                            listaTags01[cont] = 16
                        elif 800 < i < 999 and 800 < tag < 999:
                            listaTags01[cont] = 17
                elif primeraLetraTag == 'V' and primeraLetraTag == 'E' and primeraLetraI == 'V' and primeraLetraI == 'E':
                    if not lleno:
                        if primeraLetraI == 'V' and primeraLetraTag == 'V':
                            listaTags01.append(18)
                        elif primeraLetraI == 'E' and primeraLetraTag == 'E':
                            listaTags01.append(19)
                        else:
                            listaTags01.append(0)
                    else:
                        if primeraLetraI == 'V' and primeraLetraTag == 'V':
                            listaTags01[cont] = 18
                        elif primeraLetraI == 'E' and primeraLetraTag == 'E':
                            listaTags01[cont] = 19
                else:
                    if not lleno:
                        listaTags01.append(0)
                cont += 1
            lleno = True
        dicMatriz[str(key)] = listaTags01

    return dicMatriz

def convertirVectorEnValor(vector):
    """ Devuelve el valor de un vector de 0s y 1s según el número de 1s que tenga.
                    Parámetros:
                        dicTags -- vector de 1s y 0s a convertir
        """
    suma=0
    indice=0

    while indice < len(vector):
        elemento=vector[indice]
        if elemento==1:
            suma+=math.pow(2,indice)
        indice +=1
    return suma

def coeficientePearson(matrizTagsCluster):
    """ Calcula el coefiniente de correlación de Pearson
                        Parámetros:
                            matrizTagsCluster -- matriz de 0s y 1s
            """
    matriz = []
    for key in matrizTagsCluster:
        tags = matrizTagsCluster[key]
        matriz.append(tags)
    return np.corrcoef(matriz)

