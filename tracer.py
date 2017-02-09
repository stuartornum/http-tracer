import json
from flask import Flask, request, url_for, Response
app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'HEAD', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE',
                                    'PATCH', 'COPY', 'SEARCH'])
def catch_all(path):
    d = request.__dict__
    print d
    data = {}
    for i in ['REQUEST_METHOD', 'PATH_INFO', 'SERVER_PROTOCOL', 'QUERY_STRING', 'CONTENT_LENGTH', 'CONTENT_TYPE']:
        try:
            data[i] = d['environ'][i]
        except:
            pass

    headers = {}
    for i in d['environ']:
        try:
            if i[:5] == 'HTTP_':
                headers[i[5:]] = d['environ'][i]
        except:
            pass
    data['HEADERS'] = headers
    resp = Response(response=json.dumps(data), status=200, mimetype="application/json")
    return resp


def create_app():
    return app

if __name__ == '__main__':
    app.run()
