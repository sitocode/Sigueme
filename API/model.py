from app import db
from app import fields



convocatoria_fields = {
    'IDCONVOCATORIA':   fields.Integer,
    'CONVOCATORIA': fields.String,
    'CODIGO':     fields.String,
    'ESTADO': fields.String,
}


centro_fields = {
    'IDCENTRO': fields.String,
    'CENTRO':     fields.String,
}


expediente_fields = {
    'IDCONVOCATORIA':   fields.Integer,
    'IDTITULO': fields.Integer,
    'CODIGOMINISTERIO':     fields.String,
    'UNIVERSIDAD':     fields.String,
    'TITULO': fields.String,
    'ESTADO': fields.String,
    'CENTROS':fields.List(fields.Nested(centro_fields)),
}



class CONVOCATORIA(db.Model):
    __tablename__ = 'CONVOCATORIAS'
    IDCONVOCATORIA = db.Column(db.Integer, primary_key=True)
    CONVOCATORIA = db.Column(db.String(100))
    CODIGO = db.Column(db.String(25))
    ESTADO = db.Column(db.String(2))



class EXPEDIENTE_SEGUIMIENTO(db.Model):
    __tablename__ = 'EXPEDIENTES_SEGUIMIENTO'
    IDCONVOCATORIA = db.Column(db.Integer, primary_key=True)
    IDTITULO = db.Column(db.Integer, primary_key=True)
    CODIGOMINISTERIO = db.Column(db.String(20))
    TITULO = db.Column(db.String(255))
    ESTADO = db.Column(db.String(60))
    UNIVERSIDAD = db.Column(db.String(70))
    CENTROS = db.relationship('CENTROS_TITULO',
    primaryjoin='EXPEDIENTE_SEGUIMIENTO.IDTITULO == CENTROS_TITULO.IDTITULO',
    backref='EXPEDIENTE_SEGUIMIENTO' , lazy='joined')



class CENTROS_TITULO(db.Model):
    __tablename__ = 'TITULOS_CENTROS_DESC'
    IDCENTRO = db.Column(db.String(8), primary_key=True)
    IDTITULO = db.Column(db.Integer, db.ForeignKey(EXPEDIENTE_SEGUIMIENTO.IDTITULO), primary_key=True)
    CENTRO = db.Column(db.String(1000))
