#!/usr/bin/env python3
"""Index Route"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    'Renders index.html'
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
