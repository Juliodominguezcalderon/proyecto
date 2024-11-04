import matplotlib.pyplot as plt
import plotly.express as px

acciones = ["AAPL","MSFT","GOOG","NVDA"] 
   
def graficar_historico(consolidado_acciones):  
    for accion in acciones:
        datos_accion = consolidado_acciones[consolidado_acciones['Ticker'] == accion]
        plt.plot(datos_accion['Date'], datos_accion['Close'], label=accion)   
    plt.xlabel('Fecha')
    plt.ylabel('Valor Cierre')
    plt.title('Valor de cierre de las Acciones')
    plt.legend()
    plt.grid(True)
    plt.show()

def graficar_histograma(consolidado_acciones):
    for accion in acciones:
        datos_accion = consolidado_acciones[consolidado_acciones['Ticker'] == accion]
        plt.hist(datos_accion["Close"], label=accion, bins=10, alpha=0.75, edgecolor="black")
    plt.title("Histograma de precio de cierre de las acciones")
    plt.xlabel("Precio cierre")
    plt.ylabel("Frecuencia")
    plt.show()

def graficar_barras(consolidado_acciones):
    for accion in acciones:
        datos_accion = consolidado_acciones[consolidado_acciones['Ticker'] == accion]
        plt.bar(datos_accion["Ticker"], datos_accion["Close"])
    plt.title("Gráfico de barras de los precios de cierre de las acciones")
    plt.xlabel("")
    plt.ylabel("")
    plt.show()

def graficar_dispersion(consolidado_acciones):
    for accion in acciones:
        datos_accion = consolidado_acciones[consolidado_acciones['Ticker'] == accion]
        plt.scatter(datos_accion["Open"], datos_accion["Close"], marker="o") # Se tomaron dos variables cuantitativas
    plt.title("Gráfico de Dispersión")
    plt.xlabel("Precio Apertura")
    plt.ylabel("Precio Cierre")
    plt.show()

def graficar_historico(consolidado_acciones):  
    for accion in acciones:
        datos_accion = consolidado_acciones[consolidado_acciones['Ticker'] == accion]
        plt.plot(datos_accion['Date'], datos_accion['Close'], label=accion)   
    plt.xlabel('Fecha')
    plt.ylabel('Valor Cierre')
    plt.title('Valor de cierre de las Acciones')
    plt.legend()
    plt.grid(True)
    plt.show()

def graficar_historico2(consolidado_acciones):  

    fig = px.line(consolidado_acciones, x="Date", y="Close", color="Ticker", title='Precio de Cierre de Acciones')
    fig.update_xaxes(title_text='Fecha')
    fig.update_yaxes(title_text='Precio de Cierre')
    fig.show()