import os
from flask import Flask, jsonify, json, render_template
from flask_restful import reqparse, abort, Api, Resource, fields, marshal
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, Date, Float
from sqlalchemy.sql import select


app = Flask(__name__)
api = Api(app)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from model import CONVOCATORIA
from model import EXPEDIENTE_SEGUIMIENTO

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



############ Api resource routing#############################
api.add_resource(expedientesList, '/sigueme/API/expedientes/<idconvocatoria>')
api.add_resource(expediente, '/sigueme/API/expedientes/<idconvocatoria>/<id>')
api.add_resource(convocatoriasList, '/sigueme/API/convocatorias')



if __name__ == '__main__':
    app.run(debug=True)
