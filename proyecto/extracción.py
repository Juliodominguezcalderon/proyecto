import yfinance as yf
import pandas as pd

def extraer_datos(acciones, inicio, fin):
    datos = {}
    for accion in acciones:
        df = yf.download(accion, start=inicio,end=fin)
        df = df.reset_index()
        datos[accion] = df
        #df.to_csv(f"{accion}.csv")  
    print(f"datos por acción: {datos}")
    return(datos)
