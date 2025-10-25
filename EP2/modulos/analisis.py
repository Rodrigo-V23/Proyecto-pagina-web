import pandas as pd

#filtrar
def filtrar_por_rango(df, columna, minimo=None, maximo=None):
    if minimo is not None:
        df = df[df[columna] >= minimo]
    if maximo is not None:
        df = df[df[columna] <= maximo]
    return df


def filtrar_por_categoria(df, columna, valores):
    return df[df[columna].isin(valores)]


# estadisticas descriptivas

def calcular_estadisticas(df):
    return df.describe()


def tasa_condicion(df, columna):
    return round(df[columna].mean() * 100, 2)


def correlacion_salud_mental(df):
    variables = [
        "anxiety_level",
        "depression",
        "stress_level"
    ]
    return df[variables].corr()


# índices

def bienestar_general(df):
    df["wellness_score"] = (
        df["self_esteem"] +
        df["sleep_quality"] +
        df["academic_performance"] -
        df["stress_level"]
    )

    # Clasificación por intervalos
    condiciones = [
        df["wellness_score"] <= 5,
        df["wellness_score"].between(6, 10, inclusive="both"),
        df["wellness_score"] > 10
    ]
    categorias = ["Preocupante", "Estable", "Bueno"]

    df["wellness_category"] = pd.cut(
        df["wellness_score"],
        bins=[-10, 5, 10, 50],
        labels=categorias
    )

    return df[["wellness_score", "wellness_category"]]
