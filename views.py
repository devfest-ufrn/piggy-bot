import json

import apiai
from environment import env
from models import Gasto
from apistar import http, Response
from sqlalchemy.orm import Session

from schema import GastoType

ai = apiai.ApiAI(env['DIALOG_FLOW_ACCESS_TOKEN'])


def parse_message(session: Session, message: http.QueryParam):

    request = ai.text_request()
    request.lang = 'pt_BR'
    request.session_id = 1
    request.query = message
    response = json.loads(request.getresponse().read().decode('utf-8'))

    if response['result']['metadata']['intentName'] == 'registrar_gasto':
        registrar_gasto(session, response)

    return Response(response['result'], status=201)


def list_gastos(session: Session):
    queryset = session.query(Gasto).all()
    return [GastoType(gasto) for gasto in queryset]


def registrar_gasto(session: Session, response):
    gasto = Gasto()
    gasto.texto = response['result']['resolvedQuery']
    gasto.valor = response['result']['parameters']['value']

    session.add(gasto)
    session.flush()

