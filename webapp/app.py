# Aaron Burns - app.py
# a python flask app which reads input from a webpage and passes it to a trained model

# Adpated from: https://palletsprojects.com/p/flask/

import flask as fl
import base64
import numpy as np
import keras as kr

model = kr.models.load_model('../model.h5')
app = fl.Flask(__name__)

@app.route('/')
def home():
    #return app.send_static_file('webpage.html')
    return fl.render_template('app/html/webpage.html')

@app.route('/predictDigit', methods=['POST'])
def convertImage():
    # get the image from the request
    encodedImage = fl.request.values[('imgBase64')]
    # decode the dataURL
    # remove the added part of the url start from the 22 index of the image array
    decodedImage = base64.b64decode(encodedImage[22:])
    # save the image
    with open('image.png', 'wb') as f:
         f.write(decodedImage)
    # return the encoded image back to the client
    return decodedImage

def predictImage():
    image = convertImage()
    
# Recommended to have this
if __name__ == "__main__":
    app.run(debug = True)