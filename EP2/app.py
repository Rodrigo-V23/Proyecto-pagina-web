import streamlit as st
import pandas as pd
import numpy as np
from modulos.visualizacion import *
from modulos.analisis import *

st.title("Visualización de Datos - Nivel de Estrés en Estudiantes")

st.write(
    "Estos datos fueron obtenidos de [Kaggle](https://www.kaggle.com/datasets/mdsultanulislamovi/student-stress-monitoring-datasets?select=Stress_Dataset.csv) "
    "para un análisis exploratorio de datos. Contienen información sobre niveles de estrés y factores que pueden influir en el bienestar mental."
)
# carga de datos
data = pd.read_csv("data/StressLevelDataset.csv")

# Se agrega la columna gender ya que el dataset no lo tiene para hacer un filtro por genero
np.random.seed(42)
data.insert(0, 'gender', np.random.choice(['male', 'female'], size=len(data)))

# Variables disponibles dentro del dataset utilizado
fila_dato = [
    "anxiety_level", "self_esteem", "mental_health_history", "depression",
    "headache","blood_pressure", "sleep_quality", "breathing_problem", "noise_level",
    "living_conditions", "safety","basic_needs", "academic_performance", "study_load",
    "teacher_student_relationship", "future_career_concerns", "social_support",
    "peer_pressure", "extracurricular_activities", "bullying", "stress_level"
]

genero = st.radio("Filtrar por género", ["Todos", "male", "female"], horizontal=True)

# Controles interactivos para seleccionar los graficos que se quieran visualizar
tipo_grafico = st.selectbox("Tipo de gráfico", ["Barras", "Pastel", "Campana Gauss", "Matriz de Correlación"])

# Seleccion de la columna que se quiera mostrar en los graficos
columna_seleccionada = st.selectbox("Variable a analizar", fila_dato)

# Pestañas para gráfico, tabla y estadísticas descriptiva
tab1, tab2, tab3 = st.tabs(["Gráficos", "DataFrame", "Estadística descriptiva"])

# Pestaña 1 donde se muestran los graficos que se utlizaron para este analisis exploratorio de datos
with tab1:
    # Aplicacion de filtro por genero
    if genero == "Todos":
        df_grafico = data
    else:
        df_grafico = data[data["gender"] == genero]

    # Aplicacion de filtro del grafico que se quiera mostrar
    if tipo_grafico == "Barras":
        st.write("Gráfico que muestra la frecuencia de cada categoría")
        grafico_barras(df_grafico, columna_seleccionada)

    elif tipo_grafico == "Pastel":
        st.write("Gráfico que muestra la proporción de cada categoría")
        grafico_pastel(df_grafico, columna_seleccionada)

    elif tipo_grafico == "Campana Gauss":
        st.write("Gráfico que muestra la distribución de la variable elegida")
        grafico_campana_gauss(df_grafico, columna_seleccionada)

    elif tipo_grafico == "Matriz de Correlación":
        st.write("Gráfico que muestra cómo se relacionan todas las variables entre sí")
        grafico_matriz_correlacion(df_grafico, fila_dato)

# Pestaña 2 donde se muestra el dataframe utilizado
with tab2:
    st.dataframe(data, height=300, use_container_width=True)

#Pestaña 3 donde se muestra un EDA 
with tab3:
    st.subheader("Estadísticas descriptivas")
    st.dataframe(calcular_estadisticas(data))

    st.subheader("Correlación entre ansiedad, depresión y estrés")
    st.dataframe(correlacion_salud_mental(data))

    st.subheader("Bienestar general de los estudiantes por caso")
    st.dataframe(bienestar_general(data))

    st.subheader("Estadísticas separadas por género")
    # Calcular promedio de cada variable por género
    estadisticas_genero = data.groupby("gender")[fila_dato].mean()
    st.dataframe(estadisticas_genero)
