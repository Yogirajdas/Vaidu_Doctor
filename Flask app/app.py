from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

import keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image



# Define a flask app
app = Flask(__name__, template_folder='template')

# Model saved with Keras model.save()
MODEL_PATH_1 = 'models/leaf_disease_diagnosis_MobileNet3.h5'
MODEL_PATH_2 = 'models/my_h5_model.h5'
# Load your trained model
model_1 = load_model(MODEL_PATH_1)
model_2 = load_model(MODEL_PATH_2)
#model._make_predict_function()          # Necessary
# print('Model loaded. Start serving...')

# You can also use pretrained model from Keras
# Check https://keras.io/applications/
#from keras.applications.resnet50 import ResNet50
#model = ResNet50(weights='imagenet')
#model.save('')
print('Model loaded. Check http://127.0.0.1:5000/')

labels = [['Apple', 'Apple_scab'], ['Apple', 'Black_rot'], ['Apple', 'Cedar_apple_rust'], ['Apple', 'healthy'], ['Blueberry', 'healthy'], ['Cherry_(including_sour)', 'Powdery_mildew'], ['Cherry_(including_sour)', 'healthy'], ['Corn_(maize)', 'Cercospora_leaf_spot Gray_leaf_spot'], ['Corn_(maize)', 'Common_rust_'], ['Corn_(maize)', 'Northern_Leaf_Blight'], ['Corn_(maize)', 'healthy'], ['Grape', 'Black_rot'], ['Grape', 'Esca_(Black_Measles)'], ['Grape', 'Leaf_blight_(Isariopsis_Leaf_Spot)'], ['Grape', 'healthy'], ['Orange', 'Haunglongbing_(Citrus_greening)'], ['Peach', 'Bacterial_spot'], ['Peach', 'healthy'], ['Pepper,_bell', 'Bacterial_spot'], ['Pepper,_bell', 'healthy'], ['Potato', 'Early_blight'], ['Potato', 'Late_blight'], ['Potato', 'healthy'], ['Raspberry', 'healthy'], ['Soybean', 'healthy'], ['Squash', 'Powdery_mildew'], ['Strawberry', 'Leaf_scorch'], ['Strawberry', 'healthy'], ['Tomato', 'Bacterial_spot'], ['Tomato', 'Early_blight'], ['Tomato', 'Late_blight'], ['Tomato', 'Leaf_Mold'], ['Tomato', 'Septoria_leaf_spot'], ['Tomato', 'Spider_mites Two-spotted_spider_mite'], ['Tomato', 'Target_Spot'], ['Tomato', 'Tomato_Yellow_Leaf_Curl_Virus'], ['Tomato', 'Tomato_mosaic_virus'], ['Tomato', 'healthy']]
labels_1 = ['Cardiomegaly', 
          'Emphysema', 
          'Effusion', 
          'Hernia', 
          'Infiltration', 
          'Mass', 
          'Nodule', 
          'Atelectasis',
          'Pneumothorax',
          'Pleural_Thickening', 
          'Pneumonia', 
          'Fibrosis', 
          'Edema', 
          'Consolidation']









def model_1_predict(img_path, model_1):
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    x = np.expand_dims(x, axis=0)

    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
    #x = preprocess_input(x, mode='caffe')

    preds = model_1.predict(x)
    return preds

def model_2_predict(img_path, model_2):
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    x = np.expand_dims(x, axis=0)

    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
    x = preprocess_input(x, mode='caffe')

    preds = model_2.predict(x)
    return preds




@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/plant', methods =['GET', 'POST'])
def plant():
    # Main page
    return render_template('index_plant.html')

@app.route('/human', methods =['GET', 'POST'])
def human():
    # Main page
    return render_template('index_1.html')


    


@app.route('/predict_plant', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_1_predict(file_path, model_1)

        # Process your result for human
        # pred_class = preds.argmax(axis=-1)            # Simple argmax
        #pred_class = decode_predictions(preds, top=1)   # ImageNet Decode

        result = np.argmax(preds)               # Convert to string
        #result = labels[result]
        #return labels[result][0]
        ans1 = labels[result][0]
        ans2 = labels[result][1]
        data={}
        data = {'leaf':ans1,'disease':ans2}
    return data

@app.route('/predict_x-ray', methods=['GET', 'POST'])
def up():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_2_predict(file_path, model_2)

        # Process your result for human
        # pred_class = preds.argmax(axis=-1)            # Simple argmax
        if preds.any()>0.9:
            result=[]
            ans = np.where(preds>0.94,1,0)
            ans=list(ans)
            for i in range(len(labels_1)):
                if ans[0][i]==1:
                    result.append(labels_1[i])
            output = {'disease':result}
    return output



if __name__ == '__main__':
    app.run(debug=True)


