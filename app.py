from flask import Flask, request
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

@app.route("/", methods = ['POST'])
def predict():

    input_data = request.get_json()

    return '{"score":' + str(2 * float(input_data['data'])) + '}'

if __name__ == "__main__":
    app.run()