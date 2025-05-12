import os
from dataweb import DataWeb

def main():
    dataweb = DataWeb()
    df = dataweb.obtener_datos()

    if not df.empty:
        output_dir = "static/csv"
        os.makedirs(output_dir, exist_ok=True)

        csv_path = os.path.join(output_dir, "data_web.csv")
        df.to_csv(csv_path, index=False)

        print(f"CSV generado correctamente en: {csv_path}")
    else:
        print("No se obtuvieron datos.")

if __name__ == "__main__":
    main()

