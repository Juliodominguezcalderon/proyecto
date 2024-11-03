#Importamos los modulos del proyecto
import proyecto
import pandas as pd

acciones = ["AAPL","MSFT","GOOG","NVDA"] #Definimos las acciones objeto de analisis
inicio = "2004-1-1" # Definimos la fecha de inicio para analisis de las acciones
fin = "2023-12-31"  # Definimos la fecha final del analsis de las acciones

#Traemos los datos extraídos
historico_acciones = proyecto.extracción.extraer_datos(acciones, inicio, fin)

# Vista rápida de datos:
print("Información general de las columnas: \n")
print(historico_acciones.info(), "\n")
print("Resumen estadístico de las columnas: \n")
print(historico_acciones.describe())

#Visualizamos los datos
proyecto.visualización.graficar_acciones(historico_acciones)