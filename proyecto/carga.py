import pandas as pd

def cargar_datos(consolidado_acciones):
    consolidado_acciones = pd.read_csv("consolidado_acciones.csv", delimiter=",")
    consolidado_acciones.columns.values[0] = 'Indice' #Nombramos la primer columna con el nombre de Indice
    consolidado_acciones['Date'] =pd.to_datetime(consolidado_acciones['Date']) #Aseguramos que la columna Date sea en formato fecha 
    return(consolidado_acciones) 

