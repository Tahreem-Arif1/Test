import pymongo
from flask import Flask, request, jsonify
from utils import calculate

app = Flask(__name__)


@app.route('/calc-save', methods=['GET', 'POST'])
def calc():
    my_client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = my_client["test_database"]
    col = db['last_operation']

    if request.method == 'GET':
        records = [doc for doc in col.find(projection={'_id': 0})]
        no_of_documents = col.count_documents({})
        return jsonify({'records': records, 'total records': no_of_documents})

    if request.method == 'POST':
        data = request.get_json()
        a = data['op1']
        b = data['op2']
        operator = data['op']

        if operator not in ('+', '-', '/', '*'):
            return 'Unexpected Operator!!'
        else:
            result = calculate(a, b, operator)
            condition = {'operator': operator}
            updated_result = {"$set": {'op1': a, 'op2': b, 'result': result}}
            record = col.update_one(condition, updated_result, upsert=True)
            return 'Result inserted successfully !!'


if __name__ == '__main__':
    app.run(debug=True)


