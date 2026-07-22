from flask import Flask, render_template, request, redirect, url_for, Response
from functools import wraps
import json
import os

app = Flask(__name__)
DATA_FILE = 'data.json'

# --- SECURITY / AUTHENTICATION ---
# Set your desired admin username and password here
ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'andrew')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'local-dev-password-123')

def check_auth(username, password):
    """Check if a username and password match."""
    return username == ADMIN_USERNAME and password == ADMIN_PASSWORD

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to log in with proper credentials.', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

# --- DATA HELPERS ---
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

# --- ROUTES ---
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

# PROTECTED ROUTE
@app.route('/admin', methods=['GET', 'POST'])
@requires_auth  # <-- This line blocks anyone who doesn't enter the password
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
