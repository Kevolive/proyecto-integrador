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

### Ejercicio 1. Creación de DataFrame de libros con diccionario
st.subheader("""1- DataFrame de libros con Diccionario:""")

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

### Ejercicio 2: Creación de DataFrame de ciudades con lista de diccionarios
st.subheader("""2- DataFrame de ciudades con lista de diccionario:""")
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

###Ejercicio 3: Listas de listas

st.subheader("""3- DataFrame de productos con lista de listas""")
productos = [
    ["Laptop", 1200, 16],
    ["Silla", 150, 25],
    ["Libro", 20, 100],
    ["Teléfono", 800, 8]
]
df_productos = pd.DataFrame(productos, columns=["Nombre", "Precio", "Cantidad en stock"])

st.dataframe(df_productos)

st.write("### Código para crear el DataFrame de productos:")
code_productos="""" 
import streamlit as st
import pandas as pd


"productos = [
    ["Laptop", 1200, 16],
    ["Silla", 150, 25],
    ["Libro", 20, 100],
    ["Teléfono", 800, 8]
]
df_productos = pd.DataFrame(productos, columns=["Nombre", "Precio", "Cantidad en stock"])
st.DataFrame(df_productos) """
st.code(code_productos, language='python')

### Ejercicio 4: Crear dataFrame con series.
st.subheader("""4- DataFrame de estudiantes con Series""")

nombres = pd.Series(["Kevin", "Debora", "Marvin", "Paola"])
edades = pd.Series([20, 22, 19, 21])
ciuddad = pd.Series(["Medellín", "Cali", "Bogotá", "Cartagena"])

df_nombres = pd.DataFrame({'Nombres': nombres, 'Edades': edades, 'Ciudad': ciuddad})
st.dataframe(df_nombres)
st.write("### Código para crear el DataFrame de estudiantes:")

code_nombres=""" 
"import streamlit as st
import pandas as pd
"st.subheader(4- DataFrame de estudiantes con Series)

nombres = pd.Series(["Kevin", "Debora", "Marvin", "Paola"])
edades = pd.Series([20, 22, 19, 21])
ciuddad = pd.Series(["Medellín", "Cali", "Bogotá", "Cartagena"])

df_nombres = pd.DataFrame({'Nombres': nombres, 'Edades': edades, 'Ciudad': ciuddad})
st.dataframe(df_nombres)
"""
st.code(code_nombres, language='python')

### Ejercicio 5: Crear DataFrame con un archivo CSV
st.subheader("""5- DataFrame de películas con CSV""")

df_archivo = pd.read_csv("pages/data.csv", sep = ";")

st.dataframe(df_archivo)
st.write("### Código para crear el DataFrame de películas:")
code_archivo="""
import streamlit as st
import pandas as pd

df_archivo = pd.read_csv("pages/data.csv")
st.dataframe(df_archivo)
"""
st.code(code_archivo, language='python')

### Ejercicio 6: Crear DataFrame con un archivo Excel
st.subheader("""6- DataFrame  con Excel""")
df_excel = pd.read_excel("data.xlsx", engine="openpyxl")

st.dataframe(df_excel)
st.write("### Código para crear el DataFrame:")
code_excel="""
import streamlit as st
import pandas as pd
df_excel = pd.read_excel("data.xlsx")
st.dataframe(df_excel)
"""
st.code(code_excel, language='python')

### Ejercicio 7: Crear DataFrame con un archivo JSON
st.subheader("""7- DataFrame  con JSON""")

df_json = pd.read_json("data.json")

st.dataframe(df_json)

st.write("### Código para crear el DataFrame con JSON   :")
code_json="""
import streamlit as st
import pandas as pd
df_json = pd.read_json("data.json")
st.dataframe(df_json)
"""
st.code(code_json, language='python')


### Ejercicio 8: Crear DataFrame con una url
st.subheader("""8- DataFrame de películas con URL""")

df_url = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv")

st.dataframe(df_url)

st.write("### Código para crear el DataFrame de películas:")
code_url="""
import streamlit as st
import pandas as pd
df_url = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv")
st.dataframe(df_url)
"""
st.code(code_url, language='python')


