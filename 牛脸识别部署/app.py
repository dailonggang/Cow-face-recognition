from flask import Flask, jsonify, request, render_template, make_response
from PIL import Image
from frcnn import FRCNN
from PIL import Image

import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def uploadImg():
    if request.method == 'GET':
        res = make_response(render_template('index2.html'))
        return res
    elif request.method == "POST":
        if 'myImg' in request.files:
            objFile = request.files.get('myImg')
            strFileName = objFile.filename
            strFilePath = "E:/chenhongchang/实验版/img/" + strFileName
            objFile.save(strFilePath)
            sentence = strFilePath
            image_open = Image.open("%s" % sentence)

            finalimg = np.array(image_open)
            finalimg = Image.fromarray(finalimg)

            lei = FRCNN()
            tmpres = lei.detect_image(finalimg)
            res = sentence + "    " + "牛为：" + str(tmpres.atiou[0]) + "坐标为：" + str(tmpres.atiou[1]) + "   " + str( tmpres.atiou[2]) + "   " + str(tmpres.atiou[3]) + "   " + str(tmpres.atiou[4])
            return res

        else:
            err = "error"
            return err
    else:
        err = "error"
        return err


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
