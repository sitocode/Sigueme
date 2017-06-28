from flask_restful import fields
from app import db


convocatoria_fields = {
    'IDCONVOCATORIA':   fields.Integer,
    'CONVOCATORIA': fields.String,
    'CODIGO':     fields.String,
    'ESTADO': fields.String,
}

class CONVOCATORIA(db.Model):
    __tablename__ = 'CONVOCATORIAS'
    IDCONVOCATORIA = db.Column(db.Integer, primary_key=True)
    CONVOCATORIA = db.Column(db.String(100))
    CODIGO = db.Column(db.String(25))
    ESTADO = db.Column(db.String(2))
