from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/celsius-to-fahrenheit', methods=['GET', 'POST'])
def celsius_to_fahrenheit():
    if request.method == 'POST':
        celsius = request.form.get('celsius')
        if not celsius:
            return jsonify({'error': 'Please enter a Celsius value.'})
        celsius = float(celsius)
        fahrenheit = (celsius * 9/5) + 32
        return jsonify({'fahrenheit': fahrenheit})
    else:
        return "Please submit the form to convert temperature."

@app.route('/fahrenheit-to-celsius', methods=['GET', 'POST'])
def fahrenheit_to_celsius():
    if request.method == 'POST':
        fahrenheit = request.form.get('fahrenheit')
        if not fahrenheit:
            return jsonify({'error': 'Please enter a Fahrenheit value.'})
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * 5/9
        return jsonify({'celsius': celsius})
    else:
        return "Please submit the form to convert temperature."

if __name__ == '__main__':
    app.run(debug=True)