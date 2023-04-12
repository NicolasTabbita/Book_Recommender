import joblib
import pandas as pd


file = 'poly_sim_model.pkl'
scores = joblib.load(file, mmap_mode='r')

metadata = pd.read_csv('metadata.csv')
indices = pd.Series(metadata.index, index=metadata['title'])


def get_recommendations(title, scores=scores):

    """
    Funcion que recibe un titulo como input y devuelve los 5 libros mas similares

    INPUTS: 
        title: (str) titulo del libro que se quieren recomendaciones
        scores: (default archivo .pkl) que contiene simmilarity scores para la prediccion

    OUTPUT:
        DataFrame: dataframe que contiene titulos y autores de las predicciones y el libro desde el que se obtuvieron

    """

    # Encuentro el indice del titulo ingresado
    idx = indices[title]

    # Busco los scores de similaridad con este libro
    sim_scores = list(enumerate(scores[idx]))

    # Ordeno la lista de libros segun el score obtenido por cada uno
    sim_scores = sorted(sim_scores, key=lambda x:x[1], reverse=True)

    # Devuelvo los 5 mas similares (salteo el 1ro ya que el libro ingresado es siempre el mas similar a si mismo)
    sim_scores = sim_scores[1:6]

    # Busco los indices
    book_indices = [i[0] for i in sim_scores]

    # Devuelvo los titulos, autores y simmilarity scores de los libros 5 mas similares
    return pd.DataFrame({'Porque leiste': title,'Titulo': metadata['title'].iloc[book_indices], 'Autor': metadata['author'].iloc[book_indices]})
    

def get_multiple_recommendations(books, scores):

    """
    Funcion que permite tomar recomendaciones de varios libros al mismo tiempo
    Utilizando la funcion get_recommendations()

    INPUTS:
        books: (list) lista de titulos de libros de los que se quieren recomendaciones (min:1, max:5)
        scores: (list) lista de puntuaciones (de 0 al 5) que ingresa el usuario para cada libro elegido
    OUTPUT:
        dataframe: dataframe que contiene Titulo, Autor y score de las recomendaciones encontradas
    
    """

    # Si solo se pasa un libro, se utiliza la funcion get_recommendations y no se tiene en cuenta el score
    if len(books) == 1:

        return get_recommendations(books[0]).drop_duplicates(['Titulo', 'Autor'])

    # Si se pasa mas de 1 libro, estos tienen que tener un score que se usa para determinar la cantidad de
    # recomendaciones mostradas por libro
    else:    

        # Se declaran el dataframe a devolver y una lista que se usa para comprobar que no se pase 2 veces el mismo libro
        recommendations = pd.DataFrame()
        uniques = []
        
        for i in range(len(books)):

            # Se comprueba que el libro a usar no se haya pasado antes
            if books[i] not in uniques:

                # Se agrega el libro pasado por 1ra vez a la lista dee libros usados
                uniques.append(books[i])

                # Solo se obtienen recomendaciones de libros con calificacion del usuario mayor a 2
                if scores[i] > 2:

                    parcial = get_recommendations(books[i])

                    # Solo se agregan a las recomendaciones los primeros n libros siendo n el doble de la calificacion ingresada
                    recommendations = pd.concat([recommendations, parcial[:scores[i]]], ignore_index=True)

        # Se devuelven libros que no esten repetidos y que no se hayan usado para obtener recomendaciones
        try:
            return recommendations[~recommendations.Titulo.isin(uniques)].drop_duplicates(['Titulo', 'Autor'])
        except:
            return 'El/los valores asignados no son validos, intenta nuevamente. \n No te olvides que los libros con score menor a 2 no obtienen recomendaciones.'