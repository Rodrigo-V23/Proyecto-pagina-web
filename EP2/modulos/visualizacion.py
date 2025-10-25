import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def grafico_barras(df, columna, titulo="Gráfico de Barras"):
    plt.figure(figsize=(8, 5))
    df[columna].value_counts().sort_index().plot(kind='bar')
    plt.xlabel(columna)
    plt.ylabel("Frecuencia")
    plt.title(titulo)
    plt.tight_layout()
    return plt

def grafico_pastel(df, columna, titulo="Gráfico de Pastel"):
    plt.figure(figsize=(8, 5))
    df[columna].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title(titulo)
    plt.ylabel("")  
    plt.tight_layout()
    return plt

def grafico_campana_gauss(df, columna, titulo="Distribución (Campana de Gauss)"):
    plt.figure(figsize=(8, 5))
    data = df[columna]

    plt.hist(data, bins=10, density=True, alpha=0.6)

    mu, sigma = data.mean(), data.std()
    x = np.linspace(data.min(), data.max(), 100)
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(- ((x - mu)**2) / (2 * sigma**2))
    plt.plot(x, y, linewidth=2)

    plt.title(titulo)
    plt.xlabel(columna)
    plt.ylabel("Densidad")
    plt.tight_layout()
    return plt