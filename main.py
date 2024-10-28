#Importamos los modulos del proyecto
import proyecto
import pandas as pd

#acciones = {} #creamos una lista vacia
acciones = ["AAPL","MSFT","GOOG","NVDA"] #Definimos las acciones objeto de analisis
inicio = "2004-1-1" # Definimos la fecha de inicio para analisis de las acciones
fin = "2023-12-31"  # Definimos la fecha final del analsis de las acciones

#Traemos los datos extraídos
historico_acciones = proyecto.extracción.extraer_datos(acciones, inicio, fin)

#Visualizamos los datos
proyecto.visualización.graficar_acciones(historico_acciones)
