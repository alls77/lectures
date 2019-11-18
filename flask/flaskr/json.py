import flask
from json import dumps

def to_json(data):
    return json.dumps(data)


def response(code, data):
    return flask.Response(
        status=code,
        mimetype="application/json",
        response=to_json(data)
    )