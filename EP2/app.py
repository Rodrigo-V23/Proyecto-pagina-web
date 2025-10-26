import streamlit as st
import pandas as pd
import numpy as np
from modulos.visualizacion import grafico_barras, grafico_pastel, grafico_campana_gauss
from modulos.analisis import filtrar_por_rango, bienestar_general, correlacion_salud_mental, calcular_estadisticas

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

# Controles interactivos
tipo_grafico = st.selectbox("Tipo de gráfico", ["Barras", "Pastel", "Campana Gauss"])
columna_seleccionada = st.selectbox("Variable a analizar", fila_dato)

# Filtros opcionales por rango
st.sidebar.header("Filtros por rango")
columna_filtro = st.sidebar.selectbox("Columna para filtrar", fila_dato)
min_val = st.sidebar.number_input("Valor mínimo", value=int(data[columna_filtro].min()))
max_val = st.sidebar.number_input("Valor máximo", value=int(data[columna_filtro].max()))

# Aplicar filtros
data_filtrada = filtrar_por_rango(data, columna_filtro, min_val, max_val)

# Calcular bienestar
data_bienestar = bienestar_general(data_filtrada)
data_filtrada["wellness_score"] = data_bienestar["wellness_score"]
data_filtrada["wellness_category"] = data_bienestar["wellness_category"]

# Pestañas para gráfico, tabla y estadísticas
tab1, tab2, tab3 = st.tabs(["Gráficos", "DataFrame", "Estadística descriptiva"])

with tab1:
    if tipo_grafico == "Barras":
        grafico_barras(data_filtrada, columna_seleccionada)
    elif tipo_grafico == "Pastel":
        grafico_pastel(data_filtrada, columna_seleccionada)
    elif tipo_grafico == "Campana Gauss":
        grafico_campana_gauss(data_filtrada, columna_seleccionada)

with tab2:
    st.dataframe(data_filtrada, height=300, use_container_width=True)

with tab3:
    st.subheader("Estadísticas descriptivas")
    st.dataframe(calcular_estadisticas(data_filtrada))

    st.subheader("Correlación entre ansiedad, depresión y estrés")
    st.dataframe(correlacion_salud_mental(data_filtrada))

    st.subheader("Estadísticas separadas por género")
    # Calcular promedio de cada variable por género
    estadisticas_genero = data_filtrada.groupby("gender")[fila_dato].mean()
    st.dataframe(estadisticas_genero)
