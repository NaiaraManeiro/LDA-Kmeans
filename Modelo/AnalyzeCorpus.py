import operator
import statistics as stats
from collections import Counter
from math import sqrt

import numpy as np
from scipy import stats as s

def obtenerCantidades(corpus):
    """ Obtiene la cantidad de palabras de cada documento del corpus

            Parámetros:
            corpus -- lista de listas en la que cada lista está formada por la lista de palabras del documento

        """
    listaCantidades=[]
    for documento in corpus:
        if len(documento)!=1:
            listaCantidades.append(len(documento))
    return listaCantidades

def contarPalabrasDiferentes(corpus):
    """ Obtiene la cantidad de palabras diferentes de documentos
               Parámetros:
               corpus -- lista de listas en la que cada lista está formada por la lista de palabras del documento
           """
    setPalabras=set()

    for documento in corpus:
        for palabra in documento:
            setPalabras.add(palabra)
    return len(setPalabras)

def obtenerCantidadesEtiquetas(corpus):
    """ Obtiene la cantidad de etiquetas de cada documento del corpus

                Parámetros:
                corpus -- lista de listas en la que cada lista está formada por la lista de etiquetas de un documento

            """
    listaCantidades = []
    for documento in corpus:
        listaCantidades.append(len(documento))


    return listaCantidades

def media(lista):
    """ Obtiene la media de una lista

                    Parámetros:
                    lista -- lista formada por valores numéricos

                """
    return stats.mean(lista)

def mediana(lista):
    """ Obtiene la mediana de una lista

                        Parámetros:
                        lista -- lista formada por valores numéricos

                    """
    return stats.median(lista)

def moda(lista):
    """ Obtiene la media de una lista

                        Parámetros:
                        lista -- lista formada por valores numéricos

                    """

    return int(s.mode(lista)[0])

def varianza(lista):
    """ Obtiene la varianza de una lista

                        Parámetros:
                        lista -- lista formada por valores numéricos

                    """

    return np.var(lista)

def desviacion(lista):
    """ Obtiene la desviación de una lista

                        Parámetros:
                        lista -- lista formada por valores numéricos

                    """

    return sqrt(np.var(lista))

def maximo(lista):
    """ Obtiene el máximo de una lista

                        Parámetros:
                        lista -- lista formada por valores numéricos

                    """
    return max(lista)

def minimo(lista):
    """ Obtiene el mínimo de una lista

                        Parámetros:
                        lista -- lista formada por valores numéricos

                    """
    return min(lista)

def recuento(lista):
    """ Obtiene el recuento de una lista

                        Parámetros:
                        lista -- lista formada por valores numéricos

                    """
    return  len(set(lista))

def contarUnicas(lista):
    """ Obtiene la cantidad de términos únicos de una lista

                        Parámetros:
                        lista -- lista formada por valores numéricos

                    """
    diccionarioRecuento=obtenerRecuento(lista)
    unicas=0
    for key in diccionarioRecuento:
        if diccionarioRecuento[key]==1:
            unicas=unicas+1
    return unicas

def obtenerRecuento(lista):
    """ Devuelve una lista con los elementos y la cantidad de veces que se repite cada elemento en la lista

                            Parámetros:
                            lista -- lista formada por valores de cualquier tipo

                        """
    return Counter(lista)

def obtenerCantidadRepetidas(listaEtiquetas):
    """ Obtiene el número de veces que hay una lista de etiquetas repetida
                                Parámetros:
                                    listaEtiquetas -- lista de etiquetas
                    """
    dict={}
    for lista in listaEtiquetas:

        listaOrdenada=sorted(lista)
        clave=str(listaOrdenada)

        if clave not in dict.keys():

            dict[clave]=1
        else:
            dict[clave]=dict[clave]+1
    listaValores=list(dict.values())


    dictRecuento=Counter(listaValores)
    lista_multi = list(map(operator.mul, dictRecuento.values(), dictRecuento.keys()))

    del dictRecuento[1]
    cuenta=sum(list(dictRecuento.values()))
    lista_multi = list(map(operator.mul, dictRecuento.values(), dictRecuento.keys()))
    return sum(lista_multi)
