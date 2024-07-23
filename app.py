from flask import Flask, request, jsonify
from calc import Calculator

app = Flask(__name__)
calc = Calculator()

@app.route('/add', methods=['GET'])
def add():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = calc.add(a, b)
    return jsonify(result=result)

@app.route('/subtract', methods=['GET'])
def subtract():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = calc.subtract(a, b)
    return jsonify(result=result)

@app.route('/multiply', methods=['GET'])
def multiply():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = calc.multiply(a, b)
    return jsonify(result=result)

@app.route('/divide', methods=['GET'])
def divide():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    try:
        result = calc.divide(a, b)
    except ValueError as e:
        return jsonify(error=str(e)), 400
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
