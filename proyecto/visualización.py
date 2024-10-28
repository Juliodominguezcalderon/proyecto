import matplotlib.pyplot as plt

def graficar_acciones(historico_acciones):
    for accion, datos in historico_acciones.items():
        plt.plot(datos['Date'], datos['Close'], label=accion)
    plt.xlabel('Fecha')
    plt.ylabel('Valor Close')
    plt.title('Valor de cierre de las Acciones')
    plt.legend()
    plt.grid(True)
    plt.show()