from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
import urllib.parse

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Verifica si el archivo tiene extensión permitida
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        # Cargar el archivo CSV
        df = pd.read_csv(filename)

        # Realizar análisis de inconsistencias
        inconsistencies = analyze_data(df)

        # Limpiar y preparar los datos
        df_cleaned = clean_data(df)

        # Convertir a lista de diccionarios para mostrar en la interfaz
        data = df_cleaned.to_dict(orient='records')
        
        return render_template('index.html', data=data, inconsistencies=inconsistencies, filename=filename)

# Función para limpiar los datos
def clean_data(df):
    # Filtrar valores nulos o inconsistentes
    df_cleaned = df.dropna(subset=['cover_url'])

    # Filtrar filas con 'track_name' vacío o nulo
    df_cleaned = df_cleaned[df_cleaned['track_name'].notna()]
    
    return df_cleaned

# Función para analizar las inconsistencias en los datos
def analyze_data(df):
    inconsistencies = []

    # Verificar valores nulos en las columnas críticas
    if df['track_name'].isnull().any():
        inconsistencies.append("Hay valores nulos en 'track_name'.")
    if df['artist(s)_name'].isnull().any():
        inconsistencies.append("Hay valores nulos en 'artist(s)_name'.")
    if df['cover_url'].isnull().any():
        inconsistencies.append("Hay valores nulos en 'cover_url'.")

    # Verificar valores fuera de rango en columnas numéricas
    if not df['bpm'].between(60, 200).all():
        inconsistencies.append("Algunos valores de 'bpm' están fuera del rango 60-200.")
    if not df['energy_%'].between(0, 100).all():
        inconsistencies.append("Algunos valores de 'energy_%' están fuera del rango 0-100.")

    # Verificar si las URLs de imágenes son válidas
    invalid_images = df[df['cover_url'].str.contains('Not Found', na=False)]
    if not invalid_images.empty:
        inconsistencies.append(f"Se encontraron {len(invalid_images)} canciones con URL de imagen 'Not Found'.")

    # Duplicados en las canciones
    duplicates = df[df.duplicated(subset=['track_name', 'artist(s)_name'])]
    if not duplicates.empty:
        inconsistencies.append(f"Se encontraron {len(duplicates)} canciones duplicadas.")

    return inconsistencies


# Función para analizar las inconsistencias en los datos
def analyze_data_error_details(df):
    inconsistencies = []

    # Verificar valores nulos en las columnas críticas
    if df['track_name'].isnull().any():
        null_track_names = df[df['track_name'].isnull()]
        inconsistencies.append({
            "message": "Hay valores nulos en 'track_name'.",
            "details": null_track_names.to_dict(orient='records')
        })
    if df['artist(s)_name'].isnull().any():
        null_artist_names = df[df['artist(s)_name'].isnull()]
        inconsistencies.append({
            "message": "Hay valores nulos en 'artist(s)_name'.",
            "details": null_artist_names.to_dict(orient='records')
        })
    if df['cover_url'].isnull().any():
        null_cover_urls = df[df['cover_url'].isnull()]
        inconsistencies.append({
            "message": "Hay valores nulos en 'cover_url'.",
            "details": null_cover_urls.to_dict(orient='records')
        })

    # Verificar valores fuera de rango en columnas numéricas
    if not df['bpm'].between(60, 200).all():
        invalid_bpm = df[~df['bpm'].between(60, 200)]
        inconsistencies.append({
            "message": "Algunos valores de 'bpm' están fuera del rango 60-200.",
            "details": invalid_bpm.to_dict(orient='records')
        })
    if not df['energy_%'].between(0, 100).all():
        invalid_energy = df[~df['energy_%'].between(0, 100)]
        inconsistencies.append({
            "message": "Algunos valores de 'energy_%' están fuera del rango 0-100.",
            "details": invalid_energy.to_dict(orient='records')
        })

    # Verificar si las URLs de imágenes son válidas
    invalid_images = df[df['cover_url'].str.contains('Not Found', na=False)]
    if not invalid_images.empty:
        inconsistencies.append({
            "message": "Se encontraron canciones con URL de imagen 'Not Found'.",
            "details": invalid_images.to_dict(orient='records')
        })

    # Duplicados en las canciones
    duplicates = df[df.duplicated(subset=['track_name', 'artist(s)_name'])]
    if not duplicates.empty:
        inconsistencies.append({
            "message": "Se encontraron canciones duplicadas.",
            "details": duplicates.to_dict(orient='records')
        })

    return inconsistencies


# Ruta GET para recibir el nombre del archivo y mostrar inconsistencias
@app.route('/errors/<filename>', methods=['GET'])
def show_errors(filename):
    # Decodificar la URL
    decoded_filename = urllib.parse.unquote(filename)


    file_path = os.path.join(decoded_filename)

    # Verificar si el archivo existe
    if not os.path.exists(file_path):
        return render_template('error.html', error="El archivo no existe en el servidor.")

    # Verificar si el archivo tiene una extensión válida
    if not allowed_file(filename):
        return render_template('error.html', error="El archivo no es un CSV válido.")

    df = pd.read_csv(file_path)

    # Cargar y analizar el archivo CSV
    inconsistencies = analyze_data_error_details(df)

    # Pasar las inconsistencias a la plantilla
    return render_template('errors.html', inconsistencies=inconsistencies, filename=filename)


if __name__ == "__main__":
    app.run(debug=True)
