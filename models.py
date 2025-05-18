import db
from sqlalchemy import Column, Integer, String, Boolean


class Tarea(db.Base):
    __tablename__ = "tarea"
    id = Column(Integer, primary_key=True)  # Identificador único de cada tarea
    contenido = Column(String(200), nullable=False)
    hecha = Column(Boolean)

    def __init__(self, contenido, hecha):
        # El ID no es necesario crearlo, lo agrega automáticamente la DB
        self.contenido = contenido
        self.hecha = hecha

    def __repr__(self):
        return "Tarea {}: {} ({})".format(self.id, self.contenido, self.hecha)

    def __str__(self):
        return "Tarea {}: {} ({})".format(self.id, self.contenido, self.hecha)
