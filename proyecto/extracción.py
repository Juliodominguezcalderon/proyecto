import yfinance as yf
import pandas as pd

def extraer_datos(acciones, inicio, fin):
    datos_historicos =[] #creamos uns lista vacia
    for accion in acciones:
        hist_por_accion = yf.download(accion, start=inicio,end=fin)
        hist_por_accion.columns = hist_por_accion.columns.get_level_values('Price')# Nos quedamos con las columnas del nivel Price de los 2 niveles de los datos obtenidos 
        hist_por_accion = hist_por_accion.reset_index()
        hist_por_accion["Ticker"] = accion
        datos_historicos.append(hist_por_accion)
    consolidado = pd.concat(datos_historicos, ignore_index=True) #Creamos un nuevo dataframe con los historicos de las acciones y se crea un nuevo índice.
    return(consolidado)
