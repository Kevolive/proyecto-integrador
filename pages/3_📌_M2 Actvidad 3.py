from datetime import date
import streamlit as st
import pandas as pd
import numpy as np
from faker import Faker
import random

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 3")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")

st.subheader(""" Actividad 1: Practica de filtrado en Pandas (Google Colab)""")
st.markdown("""
La solución a la actividad se encuentra en el siguiente enlace de Google Colab.
Puedes abrirlo y ejecutarlo directamente en tu navegador.
""")
st.link_button("Abrir Colab", "https://colab.research.google.com/drive/1pPVlh0OY_tketv767dl9SWDYDrI2xBZj?usp=sharing")

st.subheader(""" Actividad 2: Desarrollar una aplicación de filtros dinámicos en Streamlit.""")





# Configurar Faker para Colombia
fake = Faker('es_CO')

# Establecer semilla para reproducibilidad
np.random.seed(123)
random.seed(123)
fake.seed_instance(123)

# Crear datos
n = 50
data = {
    'id': range(1, n + 1),
    'nombre_completo': [fake.name() for _ in range(n)],
    'edad': np.random.randint(15, 76, n),
    'region': random.choices(
        ['Caribe', 'Andina', 'Pacífica', 'Orinoquía', 'Amazonía'],
        weights=[0.3, 0.4, 0.15, 0.1, 0.05],
        k=n
    ),
    'municipio': random.choices(
        [
            'Barranquilla', 'Santa Marta', 'Cartagena',  # Caribe
            'Bogotá', 'Medellín', 'Tunja', 'Manizales',  # Andina
            'Cali', 'Quibdó', 'Buenaventura',           # Pacífica
            'Villavicencio', 'Yopal',                    # Orinoquía
            'Leticia', 'Puerto Inírida'                  # Amazonía
        ],
        k=n
    ),
    'ingreso_mensual': np.random.randint(800000, 12000001, n),
    'ocupacion': random.choices(
        [
            'Estudiante', 'Docente', 'Comerciante', 'Agricultor',
            'Ingeniero', 'Médico', 'Desempleado', 'Pensionado',
            'Emprendedor', 'Obrero'
        ],
        k=n
    ),
    'tipo_vivienda': random.choices(
        ['Propia', 'Arrendada', 'Familiar'],
        k=n
    ),
    'fecha_nacimiento': [
        fake.date_of_birth(minimum_age=15, maximum_age=75) for _ in range(n)
    ],
    'acceso_internet': random.choices([True, False], weights=[0.7, 0.3], k=n)
}

# Crear DataFrame
df_nuevo = pd.DataFrame(data)

# Introducir algunos valores nulos
df_nuevo.loc[3:5, 'ingreso_mensual'] = np.nan
df_nuevo.loc[15:17, 'ocupacion'] = np.nan

# Convertir fecha_nacimiento a datetime
df_nuevo['fecha_nacimiento'] = pd.to_datetime(df_nuevo['fecha_nacimiento'])


# Mostrar las primeras 5 filas
print("Primeras 5 filas del nuevo DataFrame:")
st.dataframe(df_nuevo.head())

st.title("Filtros dinámicos de las personas de la DataFrame")
st.sidebar.header("Filtros")


st.title("Filtros dinámicos")
st.sidebar.header("Activar los filtros")
filtro_df = df_nuevo.copy();

filtrar_edad = st.sidebar.checkbox("Filtrar por rango de edad")
if filtrar_edad:
    min_edad, max_edad = st.sidebar.slider("Edad:", 15, 75, (20, 40))
    filtro_df = filtro_df[filtro_df['edad'].between(min_edad, max_edad)]


filtrar_municipio=st.sidebar.checkbox("Filtrar por municipio")
if filtrar_municipio:
    municipios = df_nuevo['municipio'].unique()
    seleccionados = st.sidebar.multiselect("Selecciona municipios:", municipios)
    if seleccionados:
        filtro_df = filtro_df[filtro_df['municipio'].isin(seleccionados)]

filtrar_ingreso = st.sidebar.checkbox("Filtrar por ingresos mensuales")
if filtrar_ingreso :
    ingreso_minimo = st.sidebar.slider("Ingreso mínimo:", 800000, 12000000, step=100000)
    filtro_df = filtro_df[filtro_df['ingreso_mensual'] > ingreso_minimo]

filtro_ocupacion = st.sidebar.checkbox("Filtro ocupación")
if filtro_ocupacion:
    ocupaciones =df_nuevo['ocupacion'].dropna().unique()
    seleccionOcupacion = st.sidebar.multiselect("Seleccione las ocupaciones:", ocupaciones)
    if seleccionOcupacion:
        filtro_df= filtro_df[filtro_df['ocupacion'].isin(seleccionOcupacion)]

filtro_casa = st.sidebar.checkbox("Filtro por  personas sin vivienda propia")
if filtro_casa:
    filtro_df = filtro_df[filtro_df['tipo_vivienda']!= 'Propia']

filtro_nombres = st.sidebar.checkbox("Filtro por nombres que contienen una cadena ")
if filtro_nombres:
    nombre = st.sidebar.text_input("Contiene el nombre:")
    if nombre:
        filtro_df = filtro_df[filtro_df['nombre_completo'].str.contains(nombre, case= False, na=False)]

filtro_nacimiento = st.sidebar.checkbox(" Filtro por año de nacimiento específico ")
if filtro_nacimiento:
    anhos = sorted(df_nuevo['fecha_nacimiento'].dt.year.unique())
    anho = st.sidebar.selectbox("Año:", anhos)
    filtro_df= filtro_df[filtro_df['fecha_nacimiento'].dt.year == anho]

filtro_internet = st.sidebar.checkbox(" Filtro por acceso a internet")
if filtro_internet:
    opcion = st.sidebar.radio("Tiene acceso a internet:", ['Sí', 'No'])
    internet = True if opcion == 'Sí' else False
    filtro_df = filtro_df[filtro_df['acceso_internet']== internet]

filtro_ingresos_nulos = st.sidebar.checkbox(" Filtro por ingresos nulos")
if filtro_ingresos_nulos:
   filtro_df = filtro_df[filtro_df['ingreso_mensual'].isnull()]

filtro_df['fecha_nacimiento'] = pd.to_datetime(filtro_df['fecha_nacimiento'], errors='coerce')

# Mostrar checkbox
filtro_fechas = st.sidebar.checkbox("Filtro por rango de fechas de nacimiento")

if filtro_fechas:
    fechas = st.sidebar.date_input("Rango de fechas:", [date(1950, 1, 1), date(2009, 12, 31)])

    
    if isinstance(fechas, list) and len(fechas) == 2:
        fecha_inicia, fecha_final = pd.to_datetime(fechas[0]), pd.to_datetime(fechas[1])

       
        filtro_df = filtro_df[
            filtro_df['fecha_nacimiento'].between(fecha_inicia, fecha_final)
        ]
    else:
        st.warning("Por favor selecciona un **rango de fechas válido**.")

#Resultados

st.subheader("Resultados del filtro")
st.write(f"total registros:  {len(filtro_df)}")
st.dataframe(filtro_df)

#Edad (between)
# if st.sidebar.checkbox("Filtrar por rango de edad"):
#     min_edad, max_edad = st.sidebar.slider("Edad:", 15,75,(20,40))
#     filtro_df = filtro_df[filtro_df['edad'].between(min_edad, max_edad)]

# st.subheader("""Ejercicio 1""")
# st.write(""" Filtro por rango de edad (usando between) """)
# activar = st.checkbox("Activar el filtro de edad")
# min_edad, max_edad = st.slider("Selecciona el rango de edad:", 15, 75, (20,40))

# if activar:
#     resultado = df_nuevo[df_nuevo['edad'].between(min_edad, max_edad)]
#     st.write(f"Personas con edad entre {min_edad} y {max_edad}:")
#     st.dataframe(resultado)
# else:
#     st.write("Filtro no activado. Mostrando todos los datos:")
#     st.dataframe(df_nuevo)


# st.subheader("""Ejercicio 2""")
# st.write(""" Filtro por municipios específicos (usando isin) """)
# activar2 = st.checkbox("Activar el filtro por municipio")
# municipios = df_nuevo['municipio'].unique()
# seleccionados = st.multiselect("Seleciona los municipios", municipios)

# if activar2 and seleccionados:
#     resultadoMunicipio = df_nuevo[df_nuevo['municipio'].isin(seleccionados)]
#     st.dataframe(resultadoMunicipio)
# elif activar2:
#     st.warning("Selecciona así sea un municipio")
# else:
#     st.dataframe(df_nuevo)    

