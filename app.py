from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
DATA_FILE = 'data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

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

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        try:
            raw_content = request.form.get('json_content')
            updated_data = json.loads(raw_content)
            save_data(updated_data)
            return redirect(url_for('home'))
        except json.JSONDecodeError:
            return "Invalid JSON text format. Please check your syntax and try again.", 400

    data_str = json.dumps(load_data(), indent=4)
    return render_template('admin.html', raw_data=data_str)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
