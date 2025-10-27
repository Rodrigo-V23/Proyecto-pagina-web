import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def grafico_barras(df, columna, titulo = "Gráfico de Barras"):
    fig, ax = plt.subplots(figsize=(8, 5))
    df[columna].value_counts().sort_index().plot(kind='bar', ax=ax)
    ax.set_xlabel(columna)
    ax.set_ylabel("Frecuencia")
    ax.set_title(titulo)
    st.pyplot(fig)

def grafico_pastel(df, columna, titulo="Gráfico de Pastel"):
    fig, ax = plt.subplots(figsize=(8, 5))
    df[columna].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
    ax.set_title(titulo)
    ax.set_ylabel("")  
    st.pyplot(fig)

def grafico_campana_gauss(df, columna, titulo="Distribución (Campana de Gauss)"):
    fig, ax = plt.subplots(figsize=(8, 5))
    data = df[columna].dropna()

    ax.hist(data, bins=10, density=True, alpha=0.6)

    mu, sigma = data.mean(), data.std()
    x = np.linspace(data.min(), data.max(), 100)
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(- ((x - mu)**2) / (2 * sigma**2))
    ax.plot(x, y, linewidth=2, color='r')

    ax.set_title(titulo)
    ax.set_xlabel(columna)
    ax.set_ylabel("Densidad")
    st.pyplot(fig)
