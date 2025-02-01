from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Il file HTML che hai creato

@app.route('/api/data')
def get_data():
    return jsonify({"message": "Dati caricati con successo!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)