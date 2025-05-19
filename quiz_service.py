import pandas as pd

def cargar_preguntas():
    df = pd.read_excel("preguntas.xlsx")
    return df.to_dict(orient='records')