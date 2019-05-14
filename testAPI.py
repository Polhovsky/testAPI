from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods = ['POST'])
def predict():

    input_data = request.get_json()

    return '{"score":' + str(2 * float(input_data['data'])) + '}'

if __name__ == "__main__":
    app.run()