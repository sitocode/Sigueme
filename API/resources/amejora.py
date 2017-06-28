from flask_restful import Resource, marshal


ACCIONES_MEJORA = {
        "acciones_mejora": [
        {
            "IDCONVOCATORIA": 5,
            "IDTITULO": 1,
            "IDACCIONMEJORA": 1,
            "CORIGEN": "RA-R-OX",
            "DESCRIPCION": "DESCRIPCION 1",
            "JUSTIFICACION": "Una buena justificacion 1",
            "EVIDENCIA": "http://deva.aac.es",
            "RESPONSABLE": "Responsable numero 1",
            "FECHAINICIOPLAZO": "23/12/1980",
            "FECHAFINPLAZO": "25/12/1980",
            "FINALIZADA": "S",
            "FECHACIERRE": "",
            "DESCRIPCIONINDICADOR": "Indicador 1",
            "VALORINDICADOR": "Valor Indicador 1",
            "OBSERVACIONES": "Observaciones sobre el titulo 1, ACCION 1"
        },
        {
            "IDCONVOCATORIA": 5,
            "IDTITULO": 1,
            "IDACCIONMEJORA": 2,
            "CORIGEN": "RA-R-OX",
            "DESCRIPCION": "DESCRIPCION 1",
            "JUSTIFICACION": "Una buena justificacion 1",
            "EVIDENCIA": "http://deva.aac.es/3",
            "RESPONSABLE": "Responsable numero 1",
            "FECHAINICIOPLAZO": "23/12/1980",
            "FECHAFINPLAZO": "25/12/1980",
            "FINALIZADA": "N",
            "FECHACIERRE": "21/03/2017",
            "DESCRIPCIONINDICADOR": "Indicador 1",
            "VALORINDICADOR": "Valor Indicador 1",
            "OBSERVACIONES": "Observaciones sobre el titulo 1, ACCION 2"
        }
        ]
        }


class accionesMejoraList(Resource):
    def get(self, idtitulo, idconvocatoria):
        return ACCIONES_MEJORA["acciones_mejora"]
