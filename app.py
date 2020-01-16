import getopt
import os
import sys

import numpy
from PIL import Image
from flask import Flask, render_template, request

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


def option_prepare(argv):
    args_dict_ = {}
    opts, args = getopt.getopt(argv, "", ['host=', 'port=', 'debug=', 'options='])
    for opt, arg in opts:
        if opt == "--host":
            args_dict_['host'] = arg
        elif opt == "--port":
            args_dict_['port'] = int(arg)
        elif opt == "--debug":
            args_dict_['debug'] = arg
        elif opt == "--options":
            args_dict_['options'] = arg
    return args_dict_


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
    return render_template('style-transfer.html')


@app.route('/style-transfer.html')
def style_transefer():
    return render_template('style-transfer.html')


@app.route('/matting.html')
def matting():
    return render_template('matting.html')


@app.route('/image-fusion.html')
def image_fusion():
    return render_template('image-fusion.html')


@app.route('/style-transfer-process', methods=['post'])
def style_transfer_process():
    # print(request.form)
    style = request.form['style']
    source_pic = request.form['source'].split('.')[0]
    source_ext = request.form['source'].split('.')[1]
    style_dir = style.split(';')[0]
    style_pic = style.split(';')[1].split('.')[0]
    style_ext = style.split(';')[1].split('.')[1]
    target_pic = source_pic + '-' + style_pic
    target_ext = source_ext
    source_path = 'static/content/' + source_pic + '.' + source_ext
    img = Image.open(source_path)
    img.save('static/source-style-transfer.png')
    target_path = 'static/outputs4/' + target_pic + '-2.0.' + target_ext
    img = Image.open(target_path)
    img.save('static/target-style-transfer.png')
    return render_template('style-transfer.html')


@app.route('/image-fusion-process', methods=['post'])
def image_fusion_process():
    print(request.form)
    return render_template('image-fusion.html')


if __name__ == '__main__':
    args_dict = option_prepare(sys.argv[1:])
    print(args_dict)
    app.run(host=args_dict['host'], port=args_dict['port'])
