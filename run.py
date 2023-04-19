import streamlit as st
import pandas as pd
from model import get_multiple_recommendations

titulos = pd.read_csv('metadata.csv')

seleccion = []
score = []


st.title(':open_book: Recomendador de Libros :books:')


# A continuacion una cuadrilla de 3x5 que contiene:
#    1 checkbox para añadir/quitar un libro
#    1 selectbox para seleccionar el titulo de un libro
#    1 slider para calificar el libro elegido
# por fila

with st.container():
    col0, col1 = st.columns([2, 7])
    with col0:
        pass
    with col1:
        seleccion.append(st.selectbox(label='Titulo de un libro que te haya gustado', options=titulos['filtro'], key='sel1'))

with st.container():
    col0, col1 = st.columns([2, 7])
    with col0:
        cb0 = st.checkbox('Añadir otro libro', key='cb0')
    if cb0:
        with col1:
            seleccion.append(st.selectbox(label='Titulo de un libro que te haya gustado', options=titulos['filtro'], key='sel2'))

with st.container():
    col0, col1 = st.columns([2, 7])
    with col0:
        cb1 = st.checkbox('Añadir otro libro', key='cb1')
    if cb1:
        with col1:
            seleccion.append(st.selectbox(label='Titulo de un libro que te haya gustado', options=titulos['filtro'], key='sel3'))

with st.container():
    col0, col1 = st.columns([2, 7])
    with col0:
        cb2 = st.checkbox('Añadir otro libro', key='cb2')
    if cb2:
        with col1:
            seleccion.append(st.selectbox(label='Titulo de un libro que te haya gustado', options=titulos['filtro'], key='sel4'))

with st.container():
    col0, col1 = st.columns([2, 7])
    with col0:
        cb3 = st.checkbox('Añadir otro libro', key='cb3')
    if cb3:
        with col1:
            seleccion.append(st.selectbox(label='Titulo de un libro que te haya gustado', options=titulos['filtro'], key='sel5'))

# Boton que al ser presionado devuelve un dataframe con los resultados de las predicciones
with st.container():
    
    if st.button('Obtener recomendaciones!', type='primary', use_container_width=True):
        st.dataframe(get_multiple_recommendations(seleccion))


with st.container():
    with st.expander('¿Como funciona?'):
            st.write("""
                Luego de seleccionar uno o mas libros que hayas leido se mostraran recomendaciones.

                Para agregar/quitar un nuevo libro solo hay que seleccionar/deseleccionar los casilleros a la izquierda.
            """)