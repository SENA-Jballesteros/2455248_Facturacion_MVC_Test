from flask_controller import FlaskController
from flaskr.app import app
from flask import render_template, request, session, redirect, url_for
#import requests

class LoginController(FlaskController):
    @app.route("/", methods=['POST','GET'])
    def login():
      if request.method == 'POST':
        #s = requests.Session()
        nombre_usuario = {'nombre_usuario', request.form.get('nombre_usuario')}
        return render_template('index.html', titulo='Home') 
      return render_template('login.html', titulo='Login')