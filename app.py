from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def home():
    data = load_data()
    return render_template('index.html', data=data)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        try:
            # Parse plain-text JSON from admin editor
            raw_content = request.form.get('json_content')
            updated_data = json.loads(raw_content)
            save_data(updated_data)
            return redirect(url_for('home'))
        except json.JSONDecodeError:
            return "Invalid JSON text format. Please check your syntax and try again.", 400

    data_str = json.dumps(load_data(), indent=4)
    return render_template('admin.html', raw_data=data_str)

@app.route('/resume')
def ats_resume():
    data = load_data()
    return render_template('resume.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
