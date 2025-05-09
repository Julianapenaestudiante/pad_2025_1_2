from dataweb import DataWeb
import pandas as pd

def main():
    dataweb = DataWeb()
    df = dataweb.obtener_datos()
    if not df.empty:
        df.to_csv("data_web.csv", index=False)
        print("Archivo CSV creado correctamente.")
    else:
        print("No se obtuvieron datos.")

if __name__ == "__main__":
    main()
