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
@app.route("/predict",methods=['POST'])
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
        predictions=model.predict([[Pregnancies, Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedgreeFunction,Age]])
        if predictions==1:
            return render_template('index.html', prediction_text="Diabetic")
        else:
            return render_template('index.html', prediction_text="Non-diabetic")
    else:
        return render_template('index.html')
    
if __name__=="__main__":
    app.run(debug=True)
    

        
        
            
