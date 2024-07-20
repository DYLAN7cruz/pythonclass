
# Flask es un microframework para el desarrollo de aplicaciones web en Python. 
# Flask es conocido por ser simple, ligero y flexible.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "HOLA MUNDO !! "

if __name__ == '__main__':
    app.run(debug=True)


#para trabajar en un poroyecto de flask en python se debe tener descargado python
#luego se debe de crear un archivo padre que en este caso es app.py
#se tiene que descargar Flask con pip install Flask
#se crea el entorno virtual