from flask import Flask, request, jsonify
from utils import calculate

app = Flask(__name__)


@app.route('/calc', methods=['GET', 'POST'])
def calc():
    if request.method == 'GET':
        return 'Hello, World!'

    if request.method == 'POST':
        data = request.get_json()
        a = data['op1']
        b = data['op2']
        operator = data['op']

        if operator not in ('+', '-', '/', '*'):
            return 'Unexpected Operator!!'
        else:
            result = calculate(a, b, operator)
            return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)
