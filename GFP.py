from fastapi import FastAPI
import os
import subprocess

app = FastAPI()

@app.get("/")
async def get_json():
    def dato():
        dato = """from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ruta de inicio
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para manejar un formulario
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Obtener datos del formulario
        name = request.form['name']
        email = request.form['email']
        # Procesar los datos...
        return f"Nombre: {name}, Email: {email}"

if __name__ == '__main__':
    app.run(debug=True)

"""
        return dato

    def create():
        os.mkdir("flask-proyects")
        os.chdir("flask-proyects")
        subprocess.run(['bash', '-c', f'echo "{dato()}" > app.py']) 
    return create()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)