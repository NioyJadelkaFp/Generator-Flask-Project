from fastapi import FastAPI
import os
import subprocess

def html():
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>

    <style>
        body{
overflow: hidden;

            display: flex;
            width: 100%;
            height: 90vh;
            justify-content: center;
            align-items: center;
        }

        .Home{
            width: 90%;
            height: 90%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            border: 1px solid;
            border-radius: 10px;
        }

        .Home h1{
            font-size: 30px;
            font-family: Verdana, Geneva, Tahoma, sans-serif;
        }

        .Home p{
            margin-top: -10px;
        }

    </style>

    <section class="Home">

        <h1>CREATOR FLASK GENERATOR</h1>

        <p>Nioy Company</p>

    </section>


</body>
</html>
"""
    return html

def datos():
    datos = """#Jadelka

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ruta de inicio
@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

                    """
    return datos



app = FastAPI()

@app.get("/json")
async def get_json():
    def create():

        
        html = html()
        dato = datos()

        os.mkdir("flask-proyects")
        os.chdir("flask-proyects")
        subprocess.run(['bash', '-c', f'echo "{dato}" > app.py'])
        os.mkdir("static")
        os.mkdir("templates")
        os.chdir("templates")
        subprocess.run(['bash', '-c', f'echo "{html}" > index.html'])
        subprocess.run(['cd ..']) #cambiar por uno que funciona
        os.chdir("static")
        os.mkdir("css")
        os.chdir("css")
        subprocess.run(['bash', '-c', f'echo " " > style.css'])
        subprocess.run(['cd ..'])
        
        
    return create()
