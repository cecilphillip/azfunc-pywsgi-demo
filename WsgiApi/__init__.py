import logging

import azure.functions as func
from azf_wsgi import AzureFunctionsWsgi


def web_application(env, start_response, ):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)

    return[b'<strong>Raw WSGI application!!<strong>']


def main(req: func.HttpRequest,  context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return AzureFunctionsWsgi(web_application).main(req, context)
