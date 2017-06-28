import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, Date, Float

app = Flask(__name__)
api = Api(app)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)


from API.resources.expediente import expedientesList,expediente
from API.resources.convocatoria import convocatoriasList
from API.resources.amejora import accionesMejoraList

############ Api resource routing#############################
api.add_resource(expedientesList, '/sigueme/API/expedientes/<idconvocatoria>')
api.add_resource(expediente, '/sigueme/API/expedientes/<idconvocatoria>/<id>')
api.add_resource(convocatoriasList, '/sigueme/API/convocatorias')
api.add_resource(accionesMejoraList, '/sigueme/API/amejora/<idconvocatoria>/<idtitulo>')



if __name__ == '__main__':
    app.run(debug=True)
