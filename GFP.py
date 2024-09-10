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

        
        html_service = html()
        dato = datos()
        os.mkdir("flask-proyects")
        os.chdir("flask-proyects")
        os.mkdir("templates")
        os.mkdir("static")
        os.chdir("static")
        os.mkdir("css")
        os.mkdir("js")
        os.chdir("..")
        
        app_py = os.open("app.py",os.O_CREAT | os.O_WRONLY)
        os.write(app_py,str(dato).encode('utf-8'))
        os.chdir("templates")

        index = os.open("index.html",os.O_CREAT | os.O_WRONLY)
        os.write(index,str(html_service).encode('utf-8'))
        
        os.chdir("..")
        os.chdir("static\\css")
        styles = os.open("styles.css", os.O_CREAT | os.O_WRONLY)

        os.chdir("..")
        os.chdir("js")
        script = os.open("script.js", os.O_CREAT | os.O_WRONLY)
        os.write(script,'')
        os.chdir("..")

        os.close(app_py) 
        os.close(index) 
        os.close(styles) 
        os.close(script) 
        
    return create()
