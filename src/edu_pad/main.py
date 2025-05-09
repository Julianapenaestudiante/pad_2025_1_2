from dataweb import DataWeb
import pandas as pd



def main():
    dataweb = DataWeb()

    df = dataweb.obtener_datos()
    df = dataweb.convertir_numericos(df)
 
 



if __name__ == "__main__":
    main()