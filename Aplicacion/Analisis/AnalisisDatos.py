import sys
sys.path.append("../..")

from Modelo import FileHandler,AnalyzeCorpus

if __name__=="__main__":
    if (len(sys.argv)-1!=3):
        print("Ejecutable que analiza la distribución de palabras de los documentos calcula la media, mediana, moda, varianza \n"
              ",desviación típica y el máximo y mínimo de palabras que puede contener un documento")
        print("El ejecutable tiene que ser llamado con tres argumentos: ")
        print("Ha sido llamado con: " + str(len(sys.argv) - 1))
        print("Argumento 1: path del archivo preprocesado que contiene los documentos a analizar")
        print("Argumento 2: path del archivo que contiene las etiquetas del documento")
        print("Argumento 3: path en el que almacenar el recuento")
    else:

        listaDocumentos=FileHandler.cargarArchivoPreprocesado(sys.argv[1])

        numeroDocumentos= len(listaDocumentos)

        cantidadDocumentosRepetidos= AnalyzeCorpus.obtenerCantidadRepetidas(listaDocumentos)

        listaCantidades=AnalyzeCorpus.obtenerCantidades(listaDocumentos)
        numeroPalabras=sum(listaCantidades)
        numeroPalabrasDif=AnalyzeCorpus.contarPalabrasDiferentes(listaDocumentos)
        max=AnalyzeCorpus.maximo(listaCantidades)
        min=AnalyzeCorpus.minimo(listaCantidades)

        numDoc = "Cantidad de documentos: "+str(numeroDocumentos)
        numPalabras = "Cantidad de palabras: "+str(numeroPalabras)
        numeroPalabrasDif="Cantidad de palabras diferentes: "+str(numeroPalabrasDif)
        strMin = "Número de palabras del documento mas corto: " + str(min)
        strMax = "Número de palabras del documento mas largo: " + str(max)
        strDocumentosRep="Cantidad de documentos iguales: "+str(cantidadDocumentosRepetidos)

        resultado1 = numDoc + "\n" + numPalabras + "\n"+numeroPalabrasDif+ "\n" + strMin + "\n" + strMax +"\n"+strDocumentosRep+"\n"



        listaEtiquetasPorDocumento = FileHandler.cargarArchivoPreprocesado(
            sys.argv[2])

        listaTotalEtiquetas = FileHandler.cargarArchivoPreprocesadoEnLista(
            sys.argv[2])

        listaCantidades = AnalyzeCorpus.obtenerCantidadesEtiquetas(listaEtiquetasPorDocumento)
        # RECUENTOS:

        numDocumentos = len(listaEtiquetasPorDocumento)
        numTotalEtiquetas = sum(listaCantidades)
        cantidadCombinacionEtUnica =numeroDocumentos- AnalyzeCorpus.obtenerCantidadRepetidas(listaEtiquetasPorDocumento)
        numTipoEtiquetas = AnalyzeCorpus.recuento(listaTotalEtiquetas)
        numEtiquetasUnicas = AnalyzeCorpus.contarUnicas(listaTotalEtiquetas)


        max = AnalyzeCorpus.maximo(listaCantidades)
        min = AnalyzeCorpus.minimo(listaCantidades)

        numEtiquetas = "Cantidad de etiquetas en todos los documentos: " + str(numTotalEtiquetas)
        numEtiquetasDif = "Cantidad de etiquetas diferentes: " + str(numTipoEtiquetas)
        numEtiquetasUn = "Cantidad de etiquetas unicas: " + str(numEtiquetasUnicas)
        strMin = "Número de etiquetas del documento mas corto: " + str(min)
        strMax = "Número de etiquetas del documento mas largo: " + str(max)
        cantidadCombinacionesUnicas="Cantidad de combinaciones de etiquetas únicas en los documentos: "+str(cantidadCombinacionEtUnica)

        resultado2 = numEtiquetas + "\n" + numEtiquetasDif + "\n" + numEtiquetasUn + "\n" + strMin + "\n" + strMax + "\n" + cantidadCombinacionesUnicas



        FileHandler.guardarDocumento(resultado1+resultado2,sys.argv[3])
