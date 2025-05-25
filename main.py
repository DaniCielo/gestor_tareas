import db
from models import Tarea
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)  # Aquí se encontrará el servidor web de Flask


# La barra (el slash) se conoce como la página de inicio (página home)
@app.route('/')
def home():
    todas_las_tareas = db.session.query(Tarea).all()  # Consulta en DB
    # Las tareas se devuelven para incorporar al index.html
    return render_template("index.html", lista_de_tareas=todas_las_tareas)


@app.route('/crear-tarea', methods=['POST'])
def crear():
    tarea = Tarea(contenido=request.form['contenido-tarea'], hecha=False)
    db.session.add(tarea)  # Añadir el objeto de Tarea a la base de datos
    db.session.commit()  # Ejecutar la operación pendiente a la DB
    return redirect(url_for('home'))  # Lleva a la carga inicial de la función home


@app.route('/eliminar-tarea/<id>')
def eliminar(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).delete()  # Se busca en la DB y aquel que coincida, se elimina
    db.session.commit()  # Graba los cambios en la DB
    return redirect(url_for('home'))


@app.route('/tarea-hecha/<id>')
def hecha(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first()  # Nos trae la tarea que coincide en ID
    tarea.hecha = not tarea.hecha  # Genera el contrario
    db.session.commit()  # Grabamos en DB
    return redirect(url_for('home'))


if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)  # debug=True para que reinicie solo
