from azure.functions import (
    HttpRequest,
    HttpRequest,
    WsgiMiddleware,
    Context
)

from bottle import Bottle

app = Bottle()


@app.get('/bottle')
def hello():
    return "<strong>Bottle Application</strong>"


def main(req: HttpRequest,  context: Context) -> HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return WsgiMiddleware(app.wsgi).main(req, context)
