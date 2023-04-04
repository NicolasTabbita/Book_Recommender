import streamlit as st
import pandas as pd
from model import get_multiple_recommendations

titulos = pd.read_csv('metadata.csv')

seleccion = []
score = []

with st.container():
    with st.expander('¿Como funciona?'):
            st.write("""
                Luego de seleccionar uno o mas libros que hayas leido (y asignarle una calificacion a cada uno)
                se mostraran recomendaciones.

                Para agregar/quitar un nuevo libro solo hay que seleccionar/deseleccionar las opciones a la izquierda.

                Los libros con calificacion menor a 2 no obtienen recomendaciones.
            """)

"""
A continuacion una cuadrilla de 3x5 que contiene:
    1 checkbox para añadir/quitar un libro
    1 selectbox para seleccionar el titulo de un libro
    1 slider para calificar el libro elegido
por fila
"""
with st.container():
    col0, col1, col2 = st.columns(3)
    with col0:
        pass
    with col1:
        seleccion.append(st.selectbox(label='Titulo de un libro que te haya gustado', options=titulos['title'], key='sel1'))
    with col2:
        score.append(st.slider('Califica el libro elegido', min_value=0, max_value=5, key='scr1'))

with st.container():
    col0, col1, col2 = st.columns(3)
    with col0:
        cb0 = st.checkbox('Añadir otro libro', key='cb0')
    if cb0:
        with col1:
            seleccion.append(st.selectbox(label='Titulo de un libro que te haya gustado', options=titulos['title'], key='sel2'))
            with col2:
                score.append(st.slider('Califica el libro elegido', min_value=0, max_value=5, key='scr2', disabled=not cb0))

with st.container():
    col0, col1, col2 = st.columns(3)
    with col0:
        cb1 = st.checkbox('Añadir otro libro', key='cb1')
    if cb1:
        with col1:
            seleccion.append(st.selectbox(label='Titulo de un libro que te haya gustado', options=titulos['title'], key='sel3'))
            with col2:
                score.append(st.slider('Califica el libro elegido', min_value=0, max_value=5, key='scr3', disabled=not cb1))

with st.container():
    col0, col1, col2 = st.columns(3)
    with col0:
        cb2 = st.checkbox('Añadir otro libro', key='cb2')
    if cb2:
        with col1:
            seleccion.append(st.selectbox(label='Titulo de un libro que te haya gustado', options=titulos['title'], key='sel4'))
            with col2:
                score.append(st.slider('Califica el libro elegido', min_value=0, max_value=5, key='scr4', disabled=not cb2))

with st.container():
    col0, col1, col2 = st.columns(3)
    with col0:
        cb3 = st.checkbox('Añadir otro libro', key='cb3')
    if cb3:
        with col1:
            seleccion.append(st.selectbox(label='Titulo de un libro que te haya gustado', options=titulos['title'], key='sel5'))
            with col2:
                score.append(st.slider('Califica el libro elegido', min_value=0, max_value=5, key='scr5', disabled=not cb3))

# Boton que al ser presionado devuelve un dataframe con los resultados de las predicciones
with st.container():
    if st.button('Obtener recomendaciones!', type='primary', use_container_width=True):
        st.write(get_multiple_recommendations(seleccion, score))
