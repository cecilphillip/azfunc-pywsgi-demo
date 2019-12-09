import logging

import azure.functions as func
from azf_wsgi import AzureFunctionsWsgi

from bottle import Bottle, run

app = Bottle()


@app.get('/bottle')
def hello():
    return "<strong>Bottle Application</strong>"


def main(req: func.HttpRequest,  context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return AzureFunctionsWsgi(app.wsgi).main(req, context)
