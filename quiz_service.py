import pandas as pd

def cargar_preguntas():
    df = pd.read_excel("analisis_trading.xlsx")
    preguntas = df["Pregunta"].tolist()
    return preguntas
