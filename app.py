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


standard_to=StandardScaler()
@app.route("/outcome",methods=['POST'])
def outcome():
    if request.method=='POST':
        Pregnancies=int(request.form['Pregnancy Duration(months)'])
        Glucose=float(request.form['Glucose'])
        BloodPressure=float(request.form['BloodPressure'])
        SkinThickness=float(request.form['SkinThickness'])
        Insulin=float(request.form['Insulin'])
        BMI=float(request.form['BMI'])
        DiabetesPedgreeFunction=float(request.form['DiabetesPedgreeFunction'])
        Age=int(request.form['Age'])
        prediction=model.outcome([[Pregnancies, Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedgreeFunction,Age]])
        if prediction==1:
            return render_template('index.html', prediction_text="You are Diabetic. Consult your nearby doctor and follow the same, without any delay")
        else:
            return render_template('index.html', prediction_text="You are not a diabetic person. Stay happy and fit")
    else:
        return render_template('index.html')
    
if __name__=="__main__":
    app.run(debug=True)
    
        
        
            
