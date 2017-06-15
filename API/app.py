import os
from flask import Flask, jsonify, json, render_template
from flask_restful import reqparse, abort, Api, Resource, fields, marshal
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, Date, Float
from sqlalchemy.sql import select
os.environ["NLS_LANG"] = ".AL32UTF8"


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+cx_oracle://SEGUIMIENTO_TITULOS:segt10AG@10.79.208.55:1521/TSH1'
db = SQLAlchemy(app)



convocatoria_fields = {
    'IDCONVOCATORIA':   fields.Integer,
    'CONVOCATORIA': fields.String,
    'CODIGO':     fields.String,
    'ESTADO': fields.String,
}

expediente_fields = {
    'IDCONVOCATORIA':   fields.Integer,
    'IDTITULO': fields.Integer,
    'CODIGOMINISTERIO':     fields.String,
    'TITULO': fields.String,
    'ESTADO': fields.String,
}


parser = reqparse.RequestParser()
parser.add_argument('task')



class convocatoriasList(Resource):
    def get(self):
        return {'convocatorias': [marshal(convocatoria, convocatoria_fields) for convocatoria in CONVOCATORIA.query.all()]}


class expediente(Resource):
    def get(self, id, idconvocatoria):
        objExpediente= EXPEDIENTE_SEGUIMIENTO.query.filter_by(IDTITULO=id,IDCONVOCATORIA=idconvocatoria).first()
        return marshal(objExpediente, expediente_fields)

class expedientesList(Resource):
    def get(self, idconvocatoria):
        return {'expedientes': [marshal(expediente, expediente_fields) for expediente in EXPEDIENTE_SEGUIMIENTO.query.filter_by(IDCONVOCATORIA=idconvocatoria)]}



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




############ Api resource routing#############################
api.add_resource(expedientesList, '/sigueme/API/expedientes/<idconvocatoria>')
api.add_resource(expediente, '/sigueme/API/expedientes/<idconvocatoria>/<id>')
api.add_resource(convocatoriasList, '/sigueme/API/convocatorias')



@app.route('/list')
def list():
    return render_template('list.html')


if __name__ == '__main__':
    app.run(debug=True)
