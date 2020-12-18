Para el correcto funcionamiento del programa es necesario tener los siguientes paquetes instalados:

counter-> pip3 install counter
sklearn-> pip3 install sklearn
numpy -> pip3 install numpy
seaborn-> pip3 install seaborn
pandas-> pip3 install pandas
scipy -> pip3 install scipy
tomotopy -> pip3 install tomotopy
nltk-> pip3 install nltk


El código del proyecto se divide en tres paquetes: Aplicación, Archivos y Modelo.

Aplicación: dentro de este paquete se encuentran los ejecutables. En cada uno de ellos se especifica su función con más detalle:

	Análisis: dentro de este directorio se encuentran tres ejecutables:
		Análisis de datos: realiza el recuento inicial de los conjuntos de datos
		AnalizarNumClusters: es el ejecutable encargado de dar detalles sobre la cantidad de 					    clusters óptima a realizar.
		AnálisisDeCluster: dado el resultado de un clustering y el índice de uno de los clusters 					   devuelve gráficos con las etiquetas más relevantes y genera las 				           nubes de palabras de los topics más relevantes.
        Visualización: esta carpeta contiene dos ejecutables que generan heatmaps y nubes de palabras

    	CargarCSV: carga el CSV y realiza el preprocesado de los datos
	
	ClasificarNuevaInstancia: ejecutable que partiendo de un modelo LDA y el resultado del clustering 		sitúa una instancia desconocida en uno de los clusters. Devuelve los documentos cercanos a esta 	instancia.

	CompararCorrelacion: compara la correlación de un clustering, con dos variantes de clusters 		aleatorios
	
	GenerarLDA:Ejecutable que genera el modelo LDA partiendo de los documentos

	JensenShannon:Ejecutable que calcula la distancia Jensen Shannon entre los vectores de los 				clusters. Genera mapas de calor con la distancia entre las instancias de los 				clusters.

	KMeans:Ejecutable que calcula el cluster K-Means


	ObtenerClusterOptimo: Ejecutable que repite un cluster el número de veces indicado y elige el 					mejor

	ObtenerPalabrasTopicsModelo: Ejecutable que obtiene las n palabras más relevantes de los tópicos 						las almacena en un documento donde en cada línea se guardan las 					palabras del íésimo topic junto con su relevancia
	
	
	PredecirTopicsInstancia:Ejecutable que genera el vector de topicos de un documento partiendo de 				un modelo LDA


Modelo: Contiene las clases de la aplicación

	AnalyzeCorpus: Contiene los métodos que realizan el análisis de los documentos y de las etiquetas.

	AnalyzeResults: Contiene los métodos necesarios para realizar el análisis de los resultados.
	
	ClusterAleatorio: Clase que realiza el clustering aleatorio basado en K-Means

	Clusters: Contiene los métodos para evaluar los clusters (SSE y BSS) así como el método para 			  generar clusters aleatorios y realizar el barrido.

	Distancias: tiene los métodos para calcular las distancias

	FileHandler: Tiene los métodos relacionados con la carga y el guardado de archivos

	FilterData: Tiene los métodos necesarios para realizar el preprocesado de los datos

	K_Means: Clase que implementa el KMeans

	Transform: Tiene los métodos necesarios para aplicar el LDA

	Visualización: Clase para crear gráficos y heatmaps que ayudan a la visualización.