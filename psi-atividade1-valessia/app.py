from flask import Flask, render_template, url_for
import models

app = Flask(__name__)
secret_key = "amarelo"

@app.route('/')
def index():
    buscar_livros = models.buscar_livros()
    return render_template('index.html', livros=buscar_livros)  

@app.route('/livros')
def livros():
    buscar_livros = models.buscar_livros()
    return render_template('livros.html', livros=buscar_livros)  