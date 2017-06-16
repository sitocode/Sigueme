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


    def __init__(self, IDCONVOCATORIA, IDTITULO, CODIGOMINISTERIO, TITULO, ESTADO):
        self.IDCONVOCATORIA = IDCONVOCATORIA
        self.IDTITULO = IDTITULO
        self.CODIGOMINISTERIO = CODIGOMINISTERIO
        self.TITULO = TITULO
        self.ESTADO = ESTADO
