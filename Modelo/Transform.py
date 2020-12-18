import tomotopy


def LDA(p_min_cf, p_min_df, p_rm_top, p_k, p_alpha, p_eta,p_corpus):
    """ Devuelve una matriz de los vectores de probabilidades de los topics y el modelo generado
                                        Parámetros:
                                            p_min_cf -- mínima frecuencia de palabras en el modelo
                                            p_min_df -- mínima frecuencia de palabras en el documento
                                            p_rm_top -- cantidad de palabras comunes a eliminar del modelo
                                            p_k -- cantidad de topics a generar
                                            p_alpha -- representa la densidad documento-tema
                                            p_eta -- representa la densidad tema-palabra
                                            p_corpus -- una lista de documentos que se agregarán al modelo
                            """

    ldaModel=tomotopy.LDAModel(tw=tomotopy.TermWeight.IDF, min_cf=p_min_cf, min_df=p_min_df, rm_top=p_rm_top, k=p_k, alpha=p_alpha, eta=p_eta)

    for document in p_corpus:
        ldaModel.add_doc(document)
    ldaModel.train(500)
    lista = []
    i = 0
    for index, document in enumerate(p_corpus):
        vector=obtenerVectorTopics(ldaModel,document)
        lista.append(vector)
        i = i + 1
        if (i % 5 == 0):
            print("Modelo creado hasta documento: " + str(i))
    return lista,ldaModel


def obtenerVectorTopics(modelo,documento):
    """ Devuelve un vector con la probabilidad de los tópicos generados en el modelo pasado por parámetro
        del documento nuevo.
                                        Parámetros:
                                            modelo -- modelo LDA generado
                                            documento -- nuevo documento del que sacar los topics
                            """
    doc = modelo.make_doc(documento)
    infer = modelo.infer(doc, iter=100, tolerance=-1, workers=0, parallel=0, together=False)
    return infer[0]