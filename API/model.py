from app import db



class CONVOCATORIA(db.Model):
    __tablename__ = 'CONVOCATORIAS'
    IDCONVOCATORIA = db.Column(db.Integer, primary_key=True)
    CONVOCATORIA = db.Column(db.String(100))
    CODIGO = db.Column(db.String(25))
    ESTADO = db.Column(db.String(2))

    def __init__(self, IDCONVOCATORIA,CONVOCATORIA,CODIGO,ESTADO):
        self.IDCONVOCATORIA = IDCONVOCATORIA
        self.CONVOCATORIA = CONVOCATORIA
        self.CODIGO = CODIGO
        self.ESTADO = ESTADO



class EXPEDIENTE_SEGUIMIENTO(db.Model):
    __tablename__ = 'EXPEDIENTES_SEGUIMIENTO'
    IDCONVOCATORIA = db.Column(db.Integer, primary_key=True)
    IDTITULO = db.Column(db.Integer, primary_key=True)
    CODIGOMINISTERIO = db.Column(db.String(20))
    TITULO = db.Column(db.String(255))
    ESTADO = db.Column(db.String(60))
    UNIVERSIDAD = db.Column(db.String(70))
    CENTROS = db.relationship('CENTROS_TITULO', foreign_keys=[IDTITULO], primaryjoin='CENTROS_TITULO.IDTITULO == EXPEDIENTE_SEGUIMIENTO.IDTITULO')



class CENTROS_TITULO(db.Model):
    __tablename__ = 'TITULOS_CENTROS_DESC'
    IDCENTRO = db.Column(db.String(8), primary_key=True)
    IDTITULO = db.Column(db.Integer)
    CENTRO = db.Column(db.String(1000))
