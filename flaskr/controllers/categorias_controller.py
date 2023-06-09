
from hashlib import new
from flask_controller import FlaskController
from flaskr.app import app
from flask import render_template
from flaskr.models import db, categorias, productos, facturas, facturas_productos
from flask import request, redirect, url_for, flash

class CategoriasController(FlaskController):   
    @app.route("/categorias")
    def categorias():
        result_categorias = categorias.obtener_categorias()
        return render_template('categorias.html', titulo='Gestión de Categorias', lista_categorias=result_categorias)
    