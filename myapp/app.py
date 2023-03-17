from flask import Flask, render_template, request, redirect, url_for, jsonify
from config import DevelopmentConfig
from models import db

from Maestros.routes import maestros
from Alumnos.routes import alumnos

app = Flask(__name__)
app.config['DEBUG'] = True
app.config.from_object(DevelopmentConfig)
#csrf = CSRFProtect()

# Rutas
@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

app.register_blueprint(maestros)
app.register_blueprint(alumnos)


if __name__ == '__main__':
    # Aplicar la seguridad CSRF al inicializar la aplicación
    #csrf.init_app(app)
    # Objeto para la manipulación de la BD
    db.init_app(app)
    # Comprueba si la BD existe y genera un mapeo en automático de las tablas
    with app.app_context():
        db.create_all()
    app.run(port=3000)