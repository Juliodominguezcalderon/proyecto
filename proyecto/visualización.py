import matplotlib.pyplot as plt

acciones = ["AAPL","MSFT","GOOG","NVDA"] #Definimos las acciones objeto de analisis

def graficar_acciones(historico_acciones):  
    for accion in acciones:
        datos_accion = historico_acciones[historico_acciones['Ticker'] == accion]
        plt.plot(datos_accion['Date'], datos_accion['Close'], label=accion)   
    plt.xlabel('Fecha')
    plt.ylabel('Valor Cierre')
    plt.title('Valor de cierre de las Acciones')
    plt.legend()
    plt.grid(True)
    plt.show()