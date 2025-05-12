# Scraping de Datos Históricos del Petróleo WTI (`CL=F`) desde Yahoo Finance

Este proyecto implementa una solución automatizada de scraping para recolectar datos históricos del precio del petróleo WTI (West Texas Intermediate) desde [Yahoo Finance](https://es.finance.yahoo.com/quote/CL=F/history/). El objetivo principal es extraer la tabla de cotizaciones históricas y almacenarlas en formato CSV o Excel para análisis posterior.

## 🛠 Tecnologías y Bibliotecas Utilizadas

- Python 3.10+
- `requests` - Para hacer solicitudes HTTP a la página web.
- `BeautifulSoup` - Para analizar el contenido HTML y extraer la tabla de datos.
- `pandas` - Para estructurar y exportar los datos.
- GitHub Actions - Para integración continua.

## 📁 Estructura del Proyecto

```
pad_2025_1_2/
├── .github/workflows/python-app.yml       # Flujo de trabajo para CI
├── docs/evidencia_scraping.md             # Evidencia del proceso
├── src/edu_pad/
│   ├── __init__.py                        # Inicializador del módulo
│   ├── dataweb.py                         # Clase para scraping
│   └── main.py                            # Script principal
├── data_web.csv                           # Archivo generado con los datos
├── dataweb_limpio.xlsx                    # Datos limpios para análisis
├── README.md                              # Este archivo
├── requirements.txt                       # Librerías necesarias
└── setup.py                               # Configuración del paquete
```

## 🚀 ¿Cómo Ejecutar el Proyecto?

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Julianapenaestudiante/pad_2025_1_2.git
   cd pad_2025_1_2
   ```

2. Crear un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Activa el entorno virtual:
   ```bash
   venv\Scripts\activate
   ```

4. instala dependencias:
   ```bash
   pip install -e .
   ```

5. Ejecutar el script principal:
   ```bash
   python src/edu_pad/main.py
   ```

## 📄 Descripción de Archivos Principales

- `dataweb.py`: Contiene la lógica de scraping con `requests` y `BeautifulSoup`.
- `main.py`: Ejecuta el scraper y guarda los datos en `data_web.csv`.
- `data_web.csv`: Resultado crudo extraído desde Yahoo Finance.
- `dataweb_limpio.xlsx`: Versión depurada del conjunto de datos para análisis.

## 🧠 Autor

- JUliana Maria Peña Suarez

## 📜 Licencia

Este proyecto es solo para fines académicos y educativos.
