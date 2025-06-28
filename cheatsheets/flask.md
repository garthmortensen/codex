# flask.md

## About

**Name:** Flask (a playful reference to the 'Bottle' web framework and the idea of a small container for serving web content)

**Created:** Released in 2010 by Armin Ronacher, Flask was created as a lightweight and flexible web framework for Python. Its purpose is to provide the basics for web development without imposing structure, letting developers add only what they need.

**Similar Technologies:** Django, FastAPI, Bottle, CherryPy, Express.js

**Plain Language Definition:**
Flask is a simple toolkit for building web apps in Python. It gives you just enough to get started, so you can build your app your way.

---

## Basic Setup

```python
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/api/data')
def get_data():
    return jsonify({'message': 'Hello, API!'})

if __name__ == '__main__':
    app.run(debug=True)
```

## Running the Server

```bash
flask run                    # Run development server
flask run --host=0.0.0.0     # Run on all interfaces
flask run --port=8080        # Run on specific port
python app.py                # Run with python directly
export FLASK_ENV=development # Set development mode
```

## Routes & Methods

```python
@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        data = request.get_json()
        return jsonify({'created': data})
    return jsonify({'users': []})

@app.route('/users/<int:user_id>')
def get_user(user_id):
    return jsonify({'user_id': user_id})

@app.route('/search')
def search():
    query = request.args.get('q', '')
    return jsonify({'query': query})
```

## Request Handling

```python
from flask import request, session, redirect, url_for

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file uploaded', 400
    
    file = request.files['file']
    if file.filename == '':
        return 'No file selected', 400
    
    file.save(f'uploads/{file.filename}')
    return 'File uploaded successfully'

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    session['username'] = username
    return redirect(url_for('dashboard'))
```

## Templates & Static Files

```python
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', 
                         username=session.get('username'))

@app.route('/static/<path:filename>')
def static_files(filename):
    return app.send_static_file(filename)
```

## Data Science API

```python
import pandas as pd
from sklearn.model_selection import train_test_split

@app.route('/api/train', methods=['POST'])
def train_model():
    data = request.get_json()
    df = pd.DataFrame(data)
    
    # Simple ML pipeline
    X = df.drop('target', axis=1)
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    
    return jsonify({'status': 'Model trained', 'samples': len(df)})
```