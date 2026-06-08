from flask import Flask, jsonify, request, render_template
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from calculadora import sumar, restar, multiplicar, dividir

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sumar')
def route_sumar():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify({"operacion": "suma", "a": a, "b": b, "resultado": sumar(a, b)})

@app.route('/restar')
def route_restar():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify({"operacion": "resta", "a": a, "b": b, "resultado": restar(a, b)})

@app.route('/multiplicar')
def route_multiplicar():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify({"operacion": "multiplicacion", "a": a, "b": b, "resultado": multiplicar(a, b)})

@app.route('/dividir')
def route_dividir():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    try:
        return jsonify({"operacion": "division", "a": a, "b": b, "resultado": dividir(a, b)})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)