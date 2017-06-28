from flask_restful import Resource, marshal
from API.models.expediente import *



class expediente(Resource):
    def get(self, id, idconvocatoria):
        objExpediente= EXPEDIENTE_SEGUIMIENTO.query.filter_by(IDTITULO=id,IDCONVOCATORIA=idconvocatoria).first()
        return marshal(objExpediente, expediente_fields)

class expedientesList(Resource):
    def get(self, idconvocatoria):
        return {'expedientes': [marshal(expediente, expediente_fields) for expediente in EXPEDIENTE_SEGUIMIENTO.query.filter_by(IDCONVOCATORIA=idconvocatoria)]}
