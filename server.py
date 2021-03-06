import utils
import json
import logging
from flask_cors import CORS
from flask_restful import Resource, Api
from flask import Flask, request, jsonify, render_template

LOG_FORMAT = '%(asctime)s - %(message)s'

logging.basicConfig(filename="reqs.log",
                    filemode='a+',
                    format=LOG_FORMAT,
                    level=logging.DEBUG)

logger = logging.getLogger()

app = Flask(__name__)
api = Api(app)

CORS(app)
words = utils.read_file("words.txt")


@app.route('/data', methods=['GET', 'POST'])
def send_data():
    data = {}
    letters = request.args.get("let")
    if len(letters) > 10:
        letters = letters[:13]
    if letters:
        for i in range(3, len(letters)+1):
            perms = utils.find_perms(letters, i)
            data[str(i)] = sorted(utils.search_words(words, perms))
    return jsonify(data)


@app.route('/')
def hello_world():
    return render_template("index.html")

# @app.errorhandler(404)
# def page_not_found():
    # return render_template('error.html')
    # pass


if __name__ == '__main__':
    app.run(debug=True)
