from scipy.spatial import distance
from scipy.spatial.distance import jensenshannon


def distanciaEuclidea(vector1,vector2):
    """ Calcula la distancia Euclidea entre dos vectores
                            Parámetros:
                                vector1 -- vector de datos
                                vector2 -- vector de datos
                        """
    return distance.euclidean(vector1,vector2)

def distanciaManhattan(vector1,vector2):
    """ Calcula la distancia Manhattan entre dos vectores
                            Parámetros:
                                vector1 -- vector de datos
                                vector2 -- vector de datos
                        """
    return distance.minkowski(vector1,vector2,1)

def jensenShannonDistance(v1,v2):
    """ Calcula la distancia Jensen shannon entre dos vectores
                                Parámetros:
                                    vector1 -- vector de datos
                                    vector2 -- vector de datos
                            """
    return jensenshannon(v1,v2)

