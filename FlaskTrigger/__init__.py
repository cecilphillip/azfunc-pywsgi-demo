from azure.functions import (
    HttpRequest,
    HttpRequest,
    WsgiMiddleware,
    Context
)

from flask import Flask

app = Flask(__name__)


@app.route('/flask')
def hello():
    return "<strong>Hello From Flask</strong>"


def main(req: HttpRequest, context: Context) -> HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return WsgiMiddleware(app.wsgi_app).main(req, context)
