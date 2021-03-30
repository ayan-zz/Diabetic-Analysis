#app.py
from flask import Flask,request,render_template
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('diabetes_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict",methods=['POST'])
def predict():
    if request.method=='POST':
        Pregnancies=int(request.form['Pregnancies'])
        Glucose=float(request.form['Glucose'])
        BloodPressure=float(request.form['BloodPressure'])
        SkinThickness=float(request.form['SkinThickness'])
        Insulin=float(request.form['Insulin'])
        BMI=float(request.form['BMI'])
        DiabetesPedgreeFunction=float(request.form['DiabetesPedgreeFunction'])
        Age=int(request.form['Age'])
        predictions=model.predict([[Pregnancies, Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedgreeFunction,Age]])
        prediction_text=predictions
        
        else:
            return render_template('index.html')
        
       
    
if __name__=="__main__":
    app.run(debug=True,use_reloader=False)
    

        
        
            
