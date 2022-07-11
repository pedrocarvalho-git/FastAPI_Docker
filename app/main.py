# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:40:41 2020

@author: win10
"""
import sys
import os
sys.path.append("/code/app/")

# 1. Library imports
from typing import Dict
import uvicorn
from fastapi import FastAPI
from IrisData import IrisNewData
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
rf=pickle.load(open("app/randomforest.pkl","rb"))

# # 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index() -> Dict:
         """
         Get function of the index page.

         Returns instructions to the predict endpoint.
         """
         return {'message': os.listdir("app")}

@app.post('/predict')
def predict_iris(data:IrisNewData) -> str:
     """
     Runs the prediction of the data that came from the IrisNewData class
     and returns that prediction

     """
     data = data.dict()
     predict_df = pd.DataFrame(data, index=[0])
     prediction = rf.predict(predict_df)
     prediction = str(prediction)
     prediction_str = prediction[2:-2]
     return { 'Prediction' :  prediction_str}

#if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=8000)