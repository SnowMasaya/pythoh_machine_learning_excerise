# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('first_app.html')

if __name__ == '__main__':
    app.run(debug=True)