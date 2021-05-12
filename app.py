import logging
import re

from flask import Flask, render_template, request, jsonify
from flask.logging import default_handler

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s')
logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)
app.logger.removeHandler(default_handler)
logging.getLogger('werkzeug').setLevel(logging.ERROR)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/re', methods=['POST'])
def api_re():

    try:
        regex = request.json['regex']
        test_string = request.json['test_string']
        flags = request.json['flags']
        re_p = re.compile(regex)
        re_match = re_p.findall(test_string)
        logger.debug(f'match: {re_match}')
        logger.debug(f'flags: {flags}')

    except re.error as e:
        logger.error('re error: {}'.format(e))
        return jsonify({'result': 1, 'err_str': f'{str(e)}'})

    except KeyError:
        logger.error('Key error')
        return jsonify({'result': 2, 'err_str': 'Key error'})

    return jsonify({'result': 0, 'err_str': 'ok'})


if __name__ == '__main__':
    app.run()
