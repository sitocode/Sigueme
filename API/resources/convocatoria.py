from flask_restful import Resource, marshal
from API.models.convocatoria import *

class convocatoriasList(Resource):
    def get(self):
        return {'convocatorias': [marshal(convocatoria, convocatoria_fields) for convocatoria in CONVOCATORIA.query.all()]}
