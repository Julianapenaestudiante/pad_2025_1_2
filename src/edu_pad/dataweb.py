import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

class DataWeb:
    def __init__(self):
        self.url = "https://es.finance.yahoo.com/quote/CL=F/history/"
        self.output_dir = "static/csv"
        os.makedirs(self.output_dir, exist_ok=True)

    def obtener_datos(self):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0'
            }
            respuesta = requests.get(self.url, headers=headers)
            if respuesta.status_code != 200:
                print("La URL no respondió correctamente.")
                return pd.DataFrame()

            soup = BeautifulSoup(respuesta.text, 'html.parser')
            tabla = soup.select_one('div[data-testid="history-table"] table')

            if tabla is None:
                print("No se encontró la tabla de datos.")
                return pd.DataFrame()

            nombre_columnas = [th.get_text(strip=True) for th in tabla.thead.find_all('th')]
            filas = []

            for tr in tabla.tbody.find_all('tr'):
                columnas = [td.get_text(strip=True) for td in tr.find_all('td')]
                if len(columnas) == len(nombre_columnas):
                    filas.append(columnas)

            df = pd.DataFrame(filas, columns=nombre_columnas).rename(columns={
                'Fecha': 'fecha',
                'Abrir': 'abrir',
                'Máx.': 'max',
                'Mín.': 'min',
                'CerrarPrecio de cierre ajustado para splits.': 'cerrar',
                'Cierre ajustadoPrecio de cierre ajustado para splits y distribuciones de dividendos o plusvalías.': 'cierre_ajustado',
                'Volumen': 'volumen'
            })

            df = self.convertir_numericos(df)
            return df

        except Exception as err:
            print("Error en la función obtener_datos:", err)
            return pd.DataFrame()

    def convertir_numericos(self, df=pd.DataFrame()):
        df = df.copy()
        if len(df) > 0:
            for col in ('abrir', 'max', 'min', 'cerrar', 'cierre_ajustado', 'volumen'):
                df[col] = (
                    df[col]
                    .astype(str)
                    .str.replace(r"\.", "", regex=True)
                    .str.replace(",", ".", regex=True)
                    .astype(float)
                )
        return df
