import yfinance as yf
import pandas as pd

def extraer_acn():
    df_acn = yf.download("ACN", start="2004-1-1",end="2023-12-31")
    df_acn = pd.DataFrame(df_acn)
    df_acn = df_acn.reset_index()
    return df_acn

def extraer_crm():
    df_crm = yf.download("CRM", start="2004-1-1",end="2023-12-31")
    df_crm = pd.DataFrame(df_crm)
    df_crm = df_crm.reset_index()
    return df_crm

def extraer_msft():
    df_msft = yf.download("MSFT", start="2004-1-1",end="2023-12-31")
    df_msft = pd.DataFrame(df_msft)
    df_msft = df_msft.reset_index()#Establece la columna date    
    return df_msft

def extraer_aapl():
    df_aapl = yf.download("AAPL", start="2004-1-1",end="2023-12-31")
    df_aapl = pd.DataFrame(df_aapl)
    df_aapl = df_aapl.reset_index()
    return df_aapl