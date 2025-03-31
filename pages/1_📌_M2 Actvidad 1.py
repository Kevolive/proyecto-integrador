import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad estaremos enfocados a la creación de DataFrames,
donde aprenderemos a crear DataFrames de forma manual, utilizando listas y diccionarios.
Además, exploraremos cómo cargar datos desde archivos CSV y Excel para crear DataFrames de manera más eficiente.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")
st.subheader("Actividad 1 - Creación de DataFrames de libros con diferentes fuentes", divider=True)

### Creación de DataFrame de libros con diccionario
st.markdown("""1- DataFrame de libros con Diccionario:""")

libros = {
    "Título": ["El Principito", "Cien años de soledad", "1984", "Eva Luna"],
    "Autor": ["Antoine de Saint-Exupéry", "Gabriel García Márquez", "George Orwell", "Isabel Allende"],
    "Año de publicación": [1943, 1967, 1949, 1987],
    "Género": ["Ficción", "Realismo mágico", "Distopía", "Ficción"]
}
df_libros = pd.DataFrame(libros)


st.dataframe(df_libros)

st.write("### Código para crear el DataFrame de libros:")
code="""
import streamlit as st
import pandas as pd
libros = {
    "Título": ["El Principito", "Cien años de soledad", "1984", "Eva Luna"],
    "Autor": ["Antoine de Saint-Exupéry", "Gabriel García Márquez", "George Orwell", "Isabel Allende"],
    "Año de publicación": [1943, 1967, 1949, 1987],
    "Género": ["Ficción", "Realismo mágico", "Distopía", "Ficción"]
}
df_libros = pd.DataFrame(libros)

st.write("DataFrame de libros:")
st.dataframe(df_libros)"""
st.code(code, language='python')

### Creación de DataFrame de libros con lista de diccionarios
st.markdown("""2- DataFrame de libros con lista de diccionario:""")
ciudades = [
    {"Ciudad": "Medellín", "País": "Colombia", "Población": 2500000},
    {"Ciudad": "Bogotá", "País": "Colombia", "Población": 8000000},
    {"Ciudad": "Cali", "País": "Colombia", "Población": 2400000},
    {"Ciudad": "Cartagena", "País": "Colombia", "Población": 1000000}
]
st.write("Información de ciudades:")
df_ciudades = pd.DataFrame(ciudades)
st.dataframe(df_ciudades)
st.write("### Código para crear el DataFrame de ciudades:")

code_ciudades="""import streamlit as st
import pandas as pd
ciudades = [
    {"Ciudad": "Medellín", "País": "Colombia", "Población": 2500000},
    {"Ciudad": "Bogotá", "País": "Colombia", "Población": 8000000},
    {"Ciudad": "Cali", "País": "Colombia", "Población": 2400000},
    {"Ciudad": "Cartagena", "País": "Colombia", "Población": 1000000}
]
st.write("Información de ciudades:")
df_ciudades = pd.DataFrame(ciudades) 
st.dataframe(df_ciudades)
"""
st.code(code_ciudades, language='python')
