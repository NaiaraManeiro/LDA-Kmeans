from sklearn.decomposition import PCA
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
import collections
import seaborn as sns
from wordcloud import WordCloud
import matplotlib.colors as mcolors


def visPCA(X, numDim):
    """ Devuelve el módelo de datos con una dimensionalidad reducida
                                Parámetros:
                                    X -- datos a los que aplicarle el PCA
                                    numDim -- número de dimensiones a reducir
                    """

    pca=PCA(n_components=numDim)

    return pca.fit_transform(X)


def crearGraficoPuntos(listX, listY, colores, xlabel, ylabel,titulo,leyenda,guardar,path):
    """ Crea un gráfico de puntos con los datos introducidos
                                Parámetros:
                                    listX -- valores para el eje x
                                    listY -- valores para el eje y
                                    colores -- secuencia de colores
                                    xlabel -- valor de la etiqueta para el eje x
                                    ylabel -- valor de la etiqueta para el eje y
                                    titulo -- valor para el título
                                    leyenda -- valor para el nombre para la leyenda
                                    guardar -- boolean para guardar o no la imagen
                                    path -- directorio donde guardar la imagen
                    """

    X = np.array(listX)
    Y = np.array(listY)

    plot=plt.scatter(X, Y, c=colores, cmap=plt.get_cmap("Paired"), label=colores, edgecolor='k')

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(titulo)
    plt.legend(*plot.legend_elements(),title=leyenda)

    fig1 = plt.gcf()

    if (guardar):
        fig1.savefig(path)
    else:
        plt.show()

def grafico3d(X, y, guardar, path):
    """ Crea un gráfico 3D de puntos con los datos introducidos
                                   Parámetros:
                                       X -- valores para el eje x, y, y z
                                       y -- secuencia de colores
                                       guardar -- boolean para guardar o no la imagen
                                       path -- directorio donde guardar la imagen
                       """
    fig = plt.figure(figsize=(12, 7))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(X[:, 0], X[:, 1], X[:, 2],c=y, cmap=plt.get_cmap("Paired"), edgecolor='k')
    legend1 = ax.legend(*scatter.legend_elements(), loc="upper right", title="Clusters")
    ax.add_artist(legend1)
    ax.set_title("Resultado del K-means representado en 3D")
    if (guardar):
        fig.savefig(path)
    else:
        fig.show()

def crearGraficoBarras(listX, listY, titulo, xlabel, ylabel,minX,maxX,saltoX,guardar,path):
    """ Crea un gráfico de barras con los datos introducidos
                                   Parámetros:
                                       listX -- valores para el eje x
                                       listY -- valores para el eje y
                                       titulo -- valor para el título
                                       xlabel -- valor de la etiqueta para el eje x
                                       ylabel -- valor de la etiqueta para el eje y
                                       minX -- valor mínimo del eje x
                                       maxX -- valor máximo del eje x
                                       saltoX -- el salto entre un valor y otro en el eje x
                                       guardar -- boolean para guardar o no la imagen
                                       path -- directorio donde guardar la imagen
                       """

    x = np.array(listX)
    y = np.array(listY)
    plt.xlabel(xlabel)
    if maxX>0:
        plt.xticks(range(minX, maxX, saltoX))
    else:
        plt.xticks( rotation=90)

    plt.bar(x, y, align="center", color="blue")

    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if guardar:
        plt.savefig(path, bbox_inches='tight')
    else:
        plt.show()
    plt.clf()


def heatmap(matriz,titulo,guardar,path):
    """ Crea un heatmap con los datos introducidos
                                       Parámetros:
                                           matriz -- valores para el eje x e y
                                           titulo -- valor para el título
                                           guardar -- boolean para guardar o no la imagen
                                           path -- directorio donde guardar la imagen
                           """
    sns.set()
    ax = sns.heatmap(
        matriz,
        vmin=-0.7, vmax=1, center=0,
        cmap="cubehelix",
        square=True
    )
    ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=45,
        horizontalalignment='right'
    )

    plt.xlabel("Índice de la instancia")
    plt.ylabel("Índice de la instancia")
    plt.title(titulo)

    if guardar:
        plt.savefig(path, bbox_inches='tight')
    else:
        plt.show()

    plt.clf()

def crearGraficodePalabras(text, guardar, path):
    """ Crea una nube de palabras con los datos introducidos
                                           Parámetros:
                                               texto -- valores para el eje x e y
                                               guardar -- boolean para guardar o no la imagen
                                               path -- directorio donde guardar la imagen
                               """
    wc = WordCloud(background_color="white", max_words=1000)

    # Generate a word cloud image
    wc.generate_from_frequencies(text)

    # Display the generated image:
    # the matplotlib way:

    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")

    # lower max_font_size
    plt.axis("off")

    if guardar:
        plt.savefig(path, bbox_inches='tight')
    else:
        plt.show()

def crearGraficoPie(data,labels,guardar,path):
    """ Crea un gráfico pie con los datos introducidos
                    Parámetros:
                        data -- valores para el gráfico
                        labels -- valores para la leyenda
                        guardar -- boolean para guardar o no la imagen
                        path -- directorio donde guardar la imagen
        """

    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    def func(pct, allvals):
        absolute = int(pct / 100. * np.sum(allvals))
        if absolute>10:
            return "{:.1f}%\n".format(pct, absolute)
        else:
            return ""

    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                      textprops=dict(color="w"))

    ax.legend(wedges, labels,
              title="Etiquetas",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")

    ax.set_title("Frecuencia de etiquetas ")
    if guardar:
        plt.savefig(path, bbox_inches='tight')

    else:
        plt.show()


def graficoBarrasNubePalabras(datos):
    """ Crea un gráfico de barras con los datos introducidos
                Parámetros:
                    datos -- matriz de datos
            """

    df = pd.DataFrame(datos, columns=['word', 'topic_id', 'importance', 'word_count'])
    fig, axes = plt.subplots(2, 2, figsize=(16, 10), sharey=True, dpi=160)
    cols = [color for name, color in mcolors.TABLEAU_COLORS.items()]
    for i, ax in enumerate(axes.flatten()):
        ax.bar(x='word', height="word_count", data=df.loc[df.topic_id == i, :], color=cols[i], width=0.5, alpha=0.3,
               label='Word Count')
        ax_twin = ax.twinx()
        ax_twin.bar(x='word', height="importance", data=df.loc[df.topic_id == i, :], color=cols[i], width=0.2,
                    label='Weights')
        ax.set_ylabel('Word Count', color=cols[i])
        ax_twin.set_ylim(0, 0.060)
        ax.set_ylim(0, 5)
        ax.set_title('Topic: ' + str(i), color=cols[i], fontsize=16)
        ax.tick_params(axis='y', left=False)
        ax.set_xticklabels(df.loc[df.topic_id == i, 'word'], rotation=30, horizontalalignment='right')
        ax.legend(loc='upper left')
        ax_twin.legend(loc='upper right')

    fig.tight_layout(w_pad=2)
    fig.suptitle('Word Count and Importance of Topic Keywords', fontsize=22, y=1.05)
    plt.show()

def graficoPuntoRaya(listX, listY, titulo, xlabel, ylabel,minX,maxX,saltoX,guardar,path):

    x = np.array(listX)
    y = np.array(listY)
    plt.xlabel(xlabel)
    if maxX > 0:
        plt.xticks(range(minX, maxX,saltoX))
    else:
        plt.xticks(rotation=90)

    plt.plot(x,y, 'o')
    plt.plot(x,y, 'o-')

    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if guardar:
        plt.savefig(path, bbox_inches='tight')
    else:
        plt.show()
    plt.clf()