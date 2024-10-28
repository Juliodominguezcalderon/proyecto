import matplotlib.pyplot as plt


def grafico_acn(df_acn):
    plt.plot(df_acn["Date"],df_acn["Close"],color="blue") # type: ignore
    plt.xlabel("Fecha")
    plt.ylabel("Precio de cierre")
    plt.title("ACN")
    plt.show()

def grafico_crm(df_crm):
    plt.plot(df_crm["Date"],df_crm["Close"],color="red")
    plt.xlabel("Fecha")
    plt.ylabel("Precio de cierre")
    plt.title("CRM")
    plt.show()

def grafico_msft(df_msft):
    plt.plot(df_msft["Date"],df_msft["Close"],color="orange")
    plt.xlabel("Fecha")
    plt.ylabel("Precio de cierre")
    plt.title("Microsoft")
    plt.show()

def grafico_aapl(df_aapl):
    plt.plot(df_aapl["Date"],df_aapl["Close"],color="black")
    plt.xlabel("Fecha")
    plt.ylabel("Precio de cierre")
    plt.title("Apple")
    plt.show()


