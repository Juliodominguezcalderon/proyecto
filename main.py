#Importamos los modulos del proyecto
import proyecto

datos_acn = proyecto.extracción.extraer_acn()
datos_crm = proyecto.extracción.extraer_crm()
datos_msft = proyecto.extracción.extraer_msft()
datos_aapl = proyecto.extracción.extraer_aapl()

#Visualización de los datos
proyecto.visualización.grafico_acn(datos_acn)
proyecto.visualización.grafico_crm(datos_crm)
proyecto.visualización.grafico_msft(datos_msft)
proyecto.visualización.grafico_aapl(datos_aapl)


