from flask import Flask, render_template
import json
import os

app = Flask(__name__)
DATA_FILE = 'data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

@app.route('/')
def home():
    data = load_data()
    return render_template('index.html', data=data)

@app.route('/projects')
def projects():
    data = load_data()
    return render_template('projects.html', data=data)

@app.route('/resume')
def resume():
    data = load_data()
    return render_template('resume.html', data=data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
