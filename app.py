#!/usr/bin/env python
"""Flask application for TeamCity demo."""

from flask import Flask, jsonify, request
from calculator import Calculator

app = Flask(__name__)
calculator = Calculator()


@app.route('/')
def hello():
    """Health check endpoint."""
    return jsonify({"status": "ok", "message": "TeamCity Python Demo API is running"})


@app.route('/api/calculate', methods=['POST'])
def calculate():
    """Calculate endpoint."""
    try:
        data = request.json
        operation = data.get('operation')
        a = float(data.get('a', 0))
        b = float(data.get('b', 0))
        
        if operation == 'add':
            result = calculator.add(a, b)
        elif operation == 'subtract':
            result = calculator.subtract(a, b)
        elif operation == 'multiply':
            result = calculator.multiply(a, b)
        elif operation == 'divide':
            result = calculator.divide(a, b)
        else:
            return jsonify({"error": "Unknown operation"}), 400
        
        return jsonify({
            "operation": operation,
            "a": a,
            "b": b,
            "result": result
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/add/<float:a>/<float:b>')
def add(a, b):
    """Add two numbers."""
    return jsonify({"result": calculator.add(a, b)})


@app.route('/api/subtract/<float:a>/<float:b>')
def subtract(a, b):
    """Subtract two numbers."""
    return jsonify({"result": calculator.subtract(a, b)})


@app.route('/api/multiply/<float:a>/<float:b>')
def multiply(a, b):
    """Multiply two numbers."""
    return jsonify({"result": calculator.multiply(a, b)})


@app.route('/api/divide/<float:a>/<float:b>')
def divide(a, b):
    """Divide two numbers."""
    return jsonify({"result": calculator.divide(a, b)})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
