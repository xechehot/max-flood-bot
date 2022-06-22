from os import environ

from flask import Flask, jsonify, request, make_response, abort

# from log_config import LOG_CONFIG
# from meta import CURRENT_REVISION

# from logging.config import dictConfig
#
# dictConfig(LOG_CONFIG)
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

DEBUG = environ.get('DEBUG')


@app.route('/')
def index():
    return jsonify({'data': "Hello, World!"})


# @app.route('/meta')
# def meta():
#     return jsonify({
#         'revision': CURRENT_REVISION
#     })


@app.route('/predict', methods=['GET'])
def predict():
    data = request.json
    if 'text' not in data:
        raise Exception('Please provide text in body')
    app.logger.info(f'Predicting {data}')

    from nlp import predict
    predicted_text = predict(**data)
    result = {
        'predicted_text': predicted_text,
    }
    app.logger.info(f'Predicted: {result}')
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=DEBUG)
