# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:40:41 2020

@author: win10
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from IrisNewData import IrisNewData
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
rf=pickle.load(open("randomforest.pkl","rb"))

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Página inicial da API, usar o endpoint "/predict" para fazer a sua predição'}

@app.post('/predict')
def predict_iris(data:IrisNewData):
    data = data.dict()
    predict_df = pd.DataFrame(data, index=[0])
    #sepal_length=data['sepal_length']
    #sepal_width=data['sepal_width']
    #petal_length=data['petal_length']
    #petal_width=data['petal_width']
    prediction = rf.predict(predict_df)
    prediction = str(prediction)
    prediction_str = prediction[2:-2]
    return { 'Prediction' :  prediction_str}

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
