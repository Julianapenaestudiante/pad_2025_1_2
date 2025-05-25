import os
from dataweb import DataWeb

def main():
    dataweb = DataWeb()
    df = dataweb.obtener_datos()

    #  Mostrar los datos extraídos
    print("\n Datos extraídos de Yahoo Finance:")
    if df.empty:
        print(" No se obtuvieron datos.")
        return
    else:
        print(df.head(10))  # Mostrar solo las primeras 10 filas

        #Estadísticas básicas
        print(f"\n Total de filas extraídas: {len(df)}")
        print(f" Rango de fechas: {df['fecha'].min()} → {df['fecha'].max()}")

        #Guardar el archivo CSV
        output_dir = "static/csv"
        os.makedirs(output_dir, exist_ok=True)
        csv_path = os.path.join(output_dir, "data_web.csv")
        df.to_csv(csv_path, index=False)

        print(f"\n✅ CSV generado correctamente en: {csv_path}")

if __name__ == "__main__":
    main()


