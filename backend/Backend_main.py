import sys
import os
from flask import request, Flask
from flask_cors import CORS
from GenerateNews import *
app = Flask(__name__)

CORS(app)


@app.route('/MakeNews', methods=['GET'])
def make_news():
    input = request.args.get('topic')
    input = str(input)
    return generate_text(input, strategy="top_k")



if __name__ == '__main__':
    app.run(debug=True)


