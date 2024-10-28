import yfinance as yf
import pandas as pd

def extraer_datos(acciones, inicio, fin):
    datos = {}
    for accion in acciones:
        df = yf.download(accion, start=inicio,end=fin)
        df = df.reset_index()
        datos[accion] = df
    return(datos)
