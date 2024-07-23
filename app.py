from flask import Flask, request, jsonify
from calculator import Calculator

app = Flask(__name__)
calculator = Calculator()

@app.route('/add')
def add():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = calculator.add(a, b)
    return jsonify(result=result)

@app.route('/subtract')
def subtract():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = calculator.subtract(a, b)
    return jsonify(result=result)

@app.route('/multiply')
def multiply():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = calculator.multiply(a, b)
    return jsonify(result=result)

@app.route('/divide')
def divide():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    try:
        result = calculator.divide(a, b)
    except ValueError as e:
        return jsonify(error=str(e)), 400
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
