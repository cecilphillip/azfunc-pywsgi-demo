import logging
from flask import Flask

import azure.functions as func
from azf_wsgi import AzureFunctionsWsgi


app = Flask(__name__)


@app.route('/flask')
def hello():
    return "<strong>Hello From Flask</strong>"


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return AzureFunctionsWsgi(app.wsgi_app).main(req, context)
