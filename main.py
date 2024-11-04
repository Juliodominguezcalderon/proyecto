#Importamos los modulos del proyecto
import proyecto
import pandas as pd
import os

import proyecto.adicionar
import proyecto.carga


acciones = ["AAPL","MSFT","GOOG","NVDA"] #Definimos las acciones objeto de analisis
inicio = "2004-1-1" # Definimos la fecha de inicio para analisis de las acciones
fin = "2023-12-31"  # Definimos la fecha final del analsis de las acciones
consolidado_acciones =[]
archivo = "consolidado_acciones.csv"

#Verificamos la existencia del archivo con el historico de las acciones descargados
if not os.path.exists(archivo):
    print("El archivo no existe.\n")
    print("Ejecutamos el modulo para descargar los datos desde Yahoo Finance.\n")
    consolidado_acciones = proyecto.descargar.descargar_datos(acciones, inicio, fin)
    consolidado_acciones = proyecto.adicionar.adicionar_datos(consolidado_acciones)
    #consolidado_acciones.to_csv('consolidado_acciones.csv')
else:
    print("El archivo si existe.")
    print("Ejecutamos el modulo para cargar el historico desde una archivo.\n")
    consolidado_acciones = proyecto.carga.cargar_datos(consolidado_acciones)
    consolidado_acciones = proyecto.adicionar.adicionar_datos(consolidado_acciones)
#Cargamos los datos desde un archivo.
#consolidado_acciones = proyecto.carga.cargar_datos()

# Vista rápida de datos:
print(consolidado_acciones.head())
#print("Información general de las columnas 2: \n")
#print(consolidado_acciones.info(), "\n")
#print("Resumen estadístico de las columnas: \n")
#print(consolidado_acciones.describe())

#Visualizamos los datos
proyecto.visualización.graficar_historico(consolidado_acciones)

#proyecto.visualización.graficar_histograma(consolidado_acciones)

#proyecto.visualización.graficar_barras(consolidado_acciones)

#proyecto.visualización.graficar_dispersion(consolidado_acciones)

proyecto.visualización.graficar_historico2(consolidado_acciones)
