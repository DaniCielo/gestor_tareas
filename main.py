import db
from models import Tarea
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)  # Aquí se encontrará el servidor web de Flask


# La barra (el slash) se conoce como la página de inicio (página home)
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/crear-tarea', methods=['POST'])
def crear():
    tarea = Tarea(contenido=request.form['contenido-tarea'], hecha=False)
    db.session.add(tarea)  # Añadir el objeto de Tarea a la base de datos
    db.session.commit()  # Ejecutar la operación pendiente a la DB
    return "Tarea guardada"  # Mensaje para ver a través del navegador


if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)  # debug=True para que reinicie solo
