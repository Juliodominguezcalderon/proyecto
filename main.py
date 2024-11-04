#Importamos los modulos del proyecto
import proyecto
import pandas as pd

acciones = ["AAPL","MSFT","GOOG","NVDA"] #Definimos las acciones objeto de analisis
inicio = "2004-1-1" # Definimos la fecha de inicio para analisis de las acciones
fin = "2023-12-31"  # Definimos la fecha final del analsis de las acciones

#Traemos los datos extraídos
consolidado_acciones = proyecto.extracción.extraer_datos(acciones, inicio, fin)
consolidado_acciones["Año"] = pd.DatetimeIndex(consolidado_acciones["Date"]).year

#print(consolidado_acciones.head())
# Vista rápida de datos:
#print("Información general de las columnas: \n")
#print(consolidado_acciones.info(), "\n")
#print("Resumen estadístico de las columnas: \n")
#print(consolidado_acciones.describe())

#Visualizamos los datos
proyecto.visualización.graficar_historico(consolidado_acciones)

proyecto.visualización.graficar_histograma(consolidado_acciones)

#proyecto.visualización.graficar_barras(consolidado_acciones)

proyecto.visualización.graficar_dispersion(consolidado_acciones)

proyecto.visualización.graficar_historico2(consolidado_acciones)
