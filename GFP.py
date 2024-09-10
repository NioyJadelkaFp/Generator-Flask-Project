from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
import zipfile
import io

app = FastAPI()

# Ruta de la carpeta que deseas enviar
FOLDER_PATH = ''

@app.get("/download-folder")
def download_folder():
    # Crear un archivo ZIP en memoria
    memory_file = io.BytesIO()
    
    with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(FOLDER_PATH):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, FOLDER_PATH)  # Mantener la estructura de carpetas
                zf.write(file_path, arcname)
    
    memory_file.seek(0)  # Mover el puntero al inicio del archivo

    # Enviar el archivo ZIP
    return FileResponse(
        memory_file,
        media_type='application/zip',
        filename='folder.zip'
    )

@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
