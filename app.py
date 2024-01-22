from flask import Flask, send_from_directory, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        'imie': 'Dawid',
        'nazwisko': 'Pudlik',
        'numer_indeksu': '345351',
        'czas': current_datetime
    }
    return render_template('index.html', data=data)

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7777)
