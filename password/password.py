from flask import Flask, render_template, request, jsonify
import random
import string
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['GET'])
def generate():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.choice(chars) for _ in range(16))
    return jsonify(password=password)

if __name__ == '__main__':
    app.run(debug=True)