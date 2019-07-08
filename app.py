from flask import Flask, request
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

@app.route("/", methods = ['GET', 'POST'])
def predict():
	if request.method == 'POST':
        input_data = request.get_json()
        return '{"score":' + str(2 * float(input_data['data'])) + '}'
    else:
        return ''
if __name__ == "__main__":
    app.run()