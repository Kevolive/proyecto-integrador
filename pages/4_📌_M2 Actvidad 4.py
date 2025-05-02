
import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 4")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad se realiza para practicar el uso de los métodos `.loc` y `.iloc` de Pandas.
En esta actividad, se generará un DataFrame con datos ficticios y se utilizarán los métodos `.loc` y `.iloc` para seleccionar y modificar datos en el DataFrame.
El objetivo es entender cómo funcionan estos métodos y cuándo es apropiado usar cada uno de ellos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender la diferencia entre los métodos `.loc` y `.iloc` de Pandas.
- Aprender a seleccionar datos en un DataFrame utilizando etiquetas y posiciones.
- Practicar la modificación de datos en un DataFrame.
- Familiarizarse con la interfaz de Streamlit para la visualización y manipulación de datos.
""")

st.header("Solución")

#Se genera la DataFrame
def crear_dataframe():
    np.random.seed(42)
    return pd.DataFrame({
        "Nombre": ["Kevin", "Marvin", "Carmen", "Marta", "Paola", "Humberto", "Katiana", "Pedro", "Debora", "Jarod"],
        "Edad": np.random.randint(20, 40, 10),
        "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao", "Zaragoza", "Malaga", "Murcia", "Granada", "Alicante"],
        "Puntaje": np.random.randint(60, 100, 10)
    }, index=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
    

# Interfaz de Streamlit 

st.title("Uso de los métodos LOC vs ILOC")

# Cargar datos
df = crear_dataframe()
st.subheader("DataFrame")
st.dataframe(df)

# ------------------------------
# Selección por .loc
st.subheader("Selección con `.loc` (por etiqueta)")

fila_loc = st.selectbox("Etiqueta de fila", df.index.tolist(), key="loc_row")
columna_loc = st.selectbox("Columna", df.columns.tolist(), key="loc_col")

if st.button("Mostrar valor (.loc)"):
    valor = df.loc[fila_loc, columna_loc]
    st.success(f"Valor seleccionado: `{valor}`")
    st.code(f"df.loc['{fila_loc}', '{columna_loc}']")

# ------------------------------
# Selección por .iloc
st.subheader("Selección con `.iloc` (por posición)")

# Cambiado el rango para mostrar de 1 a 10 en lugar de 0 a 9
fila_iloc = st.selectbox("Posición de fila", list(range(1, len(df)+1)), key="iloc_row")
columna_iloc = st.selectbox("Posición de columna", list(range(1, len(df.columns)+1)), key="iloc_col")

# Obtención de las etiquetas (ajustando -1 porque iloc sigue usando índices base 0 internamente)
nombre_fila = df.index[fila_iloc-1]
nombre_columna = df.columns[columna_iloc-1]

st.write(f"Fila seleccionada: `{nombre_fila}`")
st.write(f"Columna seleccionada: `{nombre_columna}`")

if st.button("Mostrar valor (.iloc)"):
    valor = df.iloc[fila_iloc-1, columna_iloc-1]
    st.success(f"Valor seleccionado: `{valor}`")

    st.write(f"Posición seleccionada: `{fila_iloc}, {columna_iloc}`")
    st.write(f"Corresponde a:  `df.iloc[{fila_iloc-1}, {columna_iloc-1}]`")
    
    st.code(f"df.iloc[{fila_iloc-1}, {columna_iloc-1}]")
    st.code(f"df.loc['{nombre_fila}', '{nombre_columna}']")

# ------------------------------
# Modificación de datos
st.subheader("Modificar un valor")

mod_fila = st.selectbox("Fila (etiqueta)", df.index.tolist(), key="mod_row")
mod_col = st.selectbox("Columna", df.columns.tolist(), key="mod_col")
nuevo_valor = st.text_input("Nuevo valor", "")

if st.button("Aplicar cambio"):
    df.loc[mod_fila, mod_col] = nuevo_valor
    st.success(f"Valor en fila `{mod_fila}`, columna `{mod_col}` actualizado.")
    st.code(f"df.loc['{mod_fila}', '{mod_col}'] = '{nuevo_valor}'")

    st.subheader("📋 DataFrame actualizado")
    st.dataframe(df)

# ------------------------------
st.markdown("---")
st.caption("Hecho por Kevin Olivella usando Streamlit y Pandas")