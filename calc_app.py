from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/calculate', methods=['GET'])
def calculate():
    try:
        num1 = request.args.get('num1', type=float)
        num2 = request.args.get('num2', type=float)
        operation = request.args.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({"error": "Cannot divide by zero"}), 400
            result = num1 / num2
        else:
            return jsonify({"error": "Invalid operation"}), 400

        return jsonify({"result": result})

    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400


if __name__ == "__main__":
    app.run(debug=True)
