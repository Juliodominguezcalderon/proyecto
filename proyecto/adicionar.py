import pandas as pd

def adicionar_datos(consolidado_acciones):
    consolidado_acciones["Año"] = pd.DatetimeIndex(consolidado_acciones['Date']).year
    consolidado_acciones["Mes"] = pd.DatetimeIndex(consolidado_acciones['Date']).month
    consolidado_acciones["Día"] = pd.DatetimeIndex(consolidado_acciones['Date']).day
    print("se ejecutó el modulo adicionar")
    return(consolidado_acciones) 