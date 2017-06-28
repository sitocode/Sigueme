from flask_restful import fields
from app import db





acciones_mejora_fields = {
    'IDCONVOCATORIA':   fields.Integer,
    'IDTITULO': fields.Integer,
    'CODIGOMINISTERIO':     fields.String,
    'UNIVERSIDAD':     fields.String,
    'TITULO': fields.String,
    'ESTADO': fields.String,
    'CENTROS':fields.List(fields.Nested(centro_fields)),
}




class ACCION_MEJORA(db.Model):
    __tablename__ = 'ACCIONES_MEJORA'
    IDCONVOCATORIA = db.Column(db.Integer, primary_key=True)
    IDTITULO = db.Column(db.Integer, primary_key=True)
    IDACCIONMEJORA = db.Column(db.Integer, primary_key=True)
    CODIGOMINISTERIO = db.Column(db.String(20))
    TITULO = db.Column(db.String(255))
    ESTADO = db.Column(db.String(60))
    UNIVERSIDAD = db.Column(db.String(70))
