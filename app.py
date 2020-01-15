import os

import numpy
from PIL import Image
from flask import Flask, render_template, request

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/up_source', methods=['post'])
def up_source():
    print(request.files)
    img = request.files.get('photo')
    img.save('static/source.png')
    return render_template('main.html')


@app.route('/up_style', methods=['post'])
def up_style():
    print(request.files)
    img = request.files.get('photo')
    img.save('static/style.png')
    return render_template('main.html')


@app.route('/process')
def process():
    img = Image.open('static/style.png')
    img_numpy = numpy.array(img)
    img_numpy = 255 - img_numpy
    img = Image.fromarray(img_numpy)
    img.save('static/target-1.png')
    return render_template('main.html')


if __name__ == '__main__':
    app.run()
