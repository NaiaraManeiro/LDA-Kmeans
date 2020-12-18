import gensim
from nltk import WordNetLemmatizer,SnowballStemmer


def stopWords2(token):
    """ Aplica el stopWords de gensim a una palabra. Si la palabra es una stopWord devuelve un string vacío
        En caso contrario devuelve la palabra
                       Parámetros:
                           token -- String al que aplicar el stop words
    """
    if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
        return token
    else:
        return ""

def stemmer(token):
    """ Aplica el snowball stemmer de nltk a una palabra. Devuelve el String obtenido tras aplicar el stemmer
                    Parámetros:
                        token -- String al que aplicar el stemmer
    """
    stemmer = SnowballStemmer("english")
    return stemmer.stem(token)


def lemmatize(token):
    """ Aplica el lemmatizer de nltk a una palabra. Devuelve el String obtenido tras aplicar el lemmatizer
                Parámetros:
                    token -- String al que aplicar el lemmatizer
    """
    lemmatizer=WordNetLemmatizer()
    return lemmatizer.lemmatize(token)

def preprocesado(doc,pStemmer,pLemmatize,pStopwords):
    """ Realiza el preprocesado del String doc aplicandole el Stemmer, lemmatizador y el stopwords

                 Parámetros:
                        doc -- String que contiene separados por espacios los documentos sobre los que realizar el
                                preproceso.
                        pStemmer -- True si se quiere aplicar el stemmer, False en otro caso
                        pLemmatize -- True si se quiere aplicar el lemmatizer, False en otro caso
                        pStopwords -- True si se quiere aplicar el stopwords, False en otro caso
    """
    filterDoc=""
    i=0
    text=doc.split('\n')

    for j in range (len(text)-1) :

         filterText=""
         for token in text[j].split(' '):

            if(pStopwords==True):
                token=stopWords2(token)

            if (pLemmatize == True and token!=""):
                token = lemmatize(token)

            if(pStemmer==True and token!=""):
                token=stemmer(token)

            if(token!=""):
                filterText=filterText + token + ','
         i=i+1

         filterDoc=filterDoc+(filterText.rstrip(',')) + '\n'
         print("Procesado documento: " + str(i))
    return filterDoc

def preprocesadoDocumento(doc,pStemmer,pLemmatize,pStopwords):
    """ Realiza el preprocesado de un documento aplicandole el Stemmer, lemmatizador y el stopwords

                 Parámetros:
                        doc -- String que contiene un documento.
                        pStemmer -- True si se quiere aplicar el stemmer, False en otro caso
                        pLemmatize -- True si se quiere aplicar el lemmatizer, False en otro caso
                        pStopwords -- True si se quiere aplicar el stopwords, False en otro caso
    """
    filterDoc=""
    i=0
    filterText=""
    for token in doc.split(' '):
            if(pStopwords==True):
                token=stopWords2(token)

            if (pLemmatize == True and token!=""):
                token = lemmatize(token)

            if(pStemmer==True and token!=""):
                token=stemmer(token)

            if(token!=""):
                filterText=filterText + token + ','

            filterDoc=filterDoc+(filterText.rstrip(',')) + '\n'

    return filterText.rstrip(",")