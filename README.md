
# CSV Inconsistencies Analysis Tool 📊

This tool is designed to load a CSV file, analyze it for inconsistencies, and display detailed information about these issues through a web interface. The tool can identify the following types of inconsistencies:

- Null values in key fields such as 'track_name', 'artist(s)_name', and 'cover_url'.
- Values outside the expected range in numerical columns like 'bpm' and 'energy_%'.
- Invalid image URLs (when 'cover_url' is 'Not Found').
- Duplicates in songs, identifying records with the same 'track_name' and 'artist(s)_name'.

## Functionality 🚀

- **Dynamic File Upload**: Allows users to upload any CSV file for analysis.
- **Inconsistency Analysis**: Performs a thorough analysis of common inconsistencies in music-related CSV files.
- **User-Friendly Interface**: Displays inconsistencies in a card format, where the user can view the details of each inconsistency.

## Requirements 📜

- Python 3.x
- Flask
- Pandas

## Installation 🔧

1. Clone this repository:

   ```bash
   git clone https://github.com/DarwinRuiz/analizador-inconsistencias-datos-add.git
   cd your_repository
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python src/main.py
   ```

5. The tool will be available at `http://127.0.0.1:5000/` in your browser.

## Project Structure 🗂️

- **src/main.py**: The main file containing the app's logic.
- **templates/**: Folder containing HTML templates for the user interface.
  - **index.html**: The homepage to upload the CSV file.
  - **errors.html**: The details page displaying the found inconsistencies.
- **uploads/**: Folder where temporarily uploaded CSV files are stored.
- **requirements.txt**: File with the necessary dependencies to run the application.

## How to Use the Tool 🖥️

1. Go to the homepage (index.html).
2. Upload a CSV file using the upload form.
3. The tool will analyze the file and take you to a new page showing the found errors, categorized into sections.
4. If you want to go back to the homepage, simply click the "Back" button.


---

# Herramienta de Análisis de Inconsistencias en Archivos CSV 📊

Esta herramienta está diseñada para cargar un archivo CSV, analizarlo en busca de inconsistencias y mostrar los detalles de dichos problemas a través de una interfaz web. La herramienta permite identificar los siguientes tipos de inconsistencias:

- Valores nulos en campos clave como 'track_name', 'artist(s)_name' y 'cover_url'.
- Valores fuera del rango esperado en las columnas numéricas como 'bpm' y 'energy_%'.
- URLs de imágenes no válidas (cuando el valor de 'cover_url' es 'Not Found').
- Duplicados en canciones, identificando aquellos registros con el mismo 'track_name' y 'artist(s)_name'.

## Funcionalidad 🚀

- **Carga dinámica de archivos**: Permite al usuario cargar cualquier archivo CSV para su análisis.
- **Análisis de inconsistencias**: Realiza un análisis exhaustivo de las inconsistencias más comunes en archivos CSV relacionados con música.
- **Interfaz amigable**: Visualiza las inconsistencias en un formato de tarjetas, donde el usuario puede ver los detalles de cada inconsistencia.

## Requisitos 📜

- Python 3.x
- Flask
- Pandas

## Instalación 🔧

1. Clona este repositorio:

   ```bash
   git clone https://github.com/DarwinRuiz/analizador-inconsistencias-datos-add.git
   cd tu_repositorio
   ```

2. Crea un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa venv\Scripts\activate
   ```

3. Instala las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

4. Inicia la aplicación:

   ```bash
   python src/main.py
   ```

5. La herramienta estará disponible en `http://127.0.0.1:5000/` en tu navegador.

## Estructura del Proyecto 🗂️

- **src/main.py**: Archivo principal que contiene la lógica de la aplicación.
- **templates/**: Carpeta que contiene las plantillas HTML para la interfaz de usuario.
  - **index.html**: Página de inicio para cargar el archivo CSV.
  - **errors.html**: Página de detalles que muestra las inconsistencias encontradas.
- **uploads/**: Carpeta donde se almacenan los archivos CSV cargados temporalmente.
- **requirements.txt**: Archivo con las dependencias necesarias para ejecutar la aplicación.

## Cómo usar la herramienta 🖥️

1. Ve a la página de inicio (index.html).
2. Carga un archivo CSV utilizando el formulario de carga.
3. La herramienta analizará el archivo y te llevará a una nueva página con los errores encontrados, clasificados en secciones.
4. Si deseas volver a la página de inicio, simplemente haz clic en el botón de "Volver".