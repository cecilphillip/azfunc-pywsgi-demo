from azure.functions import (
    HttpRequest,
    HttpRequest,
    WsgiMiddleware,
    Context
)

from flask import Flask


def web_application(env, start_response, ):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)

    return[b'<strong>Raw WSGI application!!<strong>']


def main(req: HttpRequest,  context: Context) -> HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return WsgiMiddleware(web_application).main(req, context)
