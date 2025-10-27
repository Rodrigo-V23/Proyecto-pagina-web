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

# Cargar datos
data = pd.read_csv("EP2/data/StressLevelDataset.csv")

# Agregar columna de género aleatoria
np.random.seed(42)
data.insert(0, 'gender', np.random.choice(['male', 'female'], size=len(data)))

# Variables disponibles
fila_dato = [
    "anxiety_level", "self_esteem", "mental_health_history", "depression",
    "headache","blood_pressure", "sleep_quality", "breathing_problem", "noise_level",
    "living_conditions", "safety","basic_needs", "academic_performance", "study_load",
    "teacher_student_relationship", "future_career_concerns", "social_support",
    "peer_pressure", "extracurricular_activities", "bullying", "stress_level"
]

genero = st.radio("Filtrar por género", ["Todos", "male", "female"], horizontal=True)

# Controles interactivos
tipo_grafico = st.selectbox("Tipo de gráfico", ["Barras", "Pastel", "Campana Gauss"])
columna_seleccionada = st.selectbox("Variable a analizar", fila_dato)

# Pestañas para gráfico, tabla y estadísticas
tab1, tab2, tab3 = st.tabs(["Gráficos", "DataFrame", "Estadística descriptiva"])

with tab1:
    # Filtrar temporalmente por género solo para los gráficos
    if genero == "Todos":
        df_grafico = data
    else:
        df_grafico = data[data["gender"] == genero]

    if tipo_grafico == "Barras":
        grafico_barras(df_grafico, columna_seleccionada)
    elif tipo_grafico == "Pastel":
        grafico_pastel(df_grafico, columna_seleccionada)
    elif tipo_grafico == "Campana Gauss":
        grafico_campana_gauss(df_grafico, columna_seleccionada)

with tab2:
    st.dataframe(data, height=300, use_container_width=True)

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
