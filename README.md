# Diabetic-Analysis
Data set from NIDDK. We are using the dataset all patients here belong to the Pima Indian heritage (subgroup of Native Americans), and are females of ages 21 and above.
## Data Description
We have saved all the data in .csv file. All action will be performed upon this data set.
The following features have been provided to help us predict whether a person is diabetic or not:
#### Pregnancies: Number of times pregnant
####  Glucose: Plasma glucose concentration over 2 hours in an oral glucose tolerance test
#### BloodPressure: Diastolic blood pressure (mm Hg)
#### SkinThickness: Triceps skin fold thickness (mm)
#### Insulin: 2-Hour serum insulin (mu U/ml)
#### BMI: Body mass index (weight in kg/(height in m)2)
#### DiabetesPedigreeFunction: Diabetes pedigree function (a function which scores likelihood of diabetes based on family history)
#### Age: Age (years)
#### Outcome: Class variable (0 if non-diabetic, 1 if diabetic)

###Project Task:
1. Data Exploration:
Check the balance of the data by plotting the count of outcomes by their value. Describe your findings and plan future course of action. Create scatter charts between the pair of variables to understand the relationships. Describe your findings. Perform correlation analysis.Visually explore it using a heat map.

![download](https://user-images.githubusercontent.com/64850346/112982752-7763d100-917a-11eb-9ecb-a8b302cf7914.png)
By finding the count of outcomes, we can easily say that the dataset is balanced and there is no need of balancing. We get 500 as non-diabetic and 268 as diabetic. likey 53.6% of data available has diabetic patients.
On further course of action we will decide the most dependent variable for a patient to be diabetic.
![download (1)](https://user-images.githubusercontent.com/64850346/112982900-a8440600-917a-11eb-9dd2-c46efca2b72b.png)

![download (2)](https://user-images.githubusercontent.com/64850346/112983041-d0336980-917a-11eb-9d6e-68aaee2005d0.png)

Observations:
 i) We get good correlation on Age and Pregnancies of 0.54.
 ii) Diabetic patients has high level of glucose of correlation 0.49. Further more we find amount of glucose,BMI,and age are the best perforing factors to be a diabetic/ non-  diabetic.
 iii) Insulin level is high with glucose. Having correlation of 0.42. But doesnt mean they are diabetic.
 iv) Glucose can be the primary factor for a diabetic person with underlying factors may be BMI and age.
 v) Blood pressure is very badly correlated with outcome. This means a diabetic patient cant have high blood pressure. High insulin level doesnt means he/she is diabetic.
 
 2.Data Modeling:
  l. Devise strategies for model building. It is important to decide the right validation framework. Express your thought process.
 ll. Apply an appropriate classification algorithm to build a model. Compare various models with the results from KNN algorithm.
 
 Undergone observation based on algorithms: i) Logistic Regression ii) Decision Tree iii) KNNeighbour iv) XG Boost v)Gaussian NB
 The baseline model performance can be improved. Based on EDA we are going to take following actions on raw data:
 Imputation of zero values after grouping the data on different parameters
  a. Feature Engineering
  b. Using PCA since there were correlations found in the features
  c. Hyper-parameter tuning the models
-The feature Glucose has considerably less number of missing entries which can be imputed by simple mean values.
-Although we can impute the missing values in BMI with respect to the mean of each outcome but using TARGET Variable to impute values.
-Let us fill the missing values by overall mean of the entire data in the BMI column.
We had succesfully imputed the missing values not by just random mean or zero valus.The missing values are imputed depending as per co-relation observed with other features and binning the age, BMI and Glucose column. Later on removed the bins.
Although we havent seen much change in feature engg. We found #### Glucose as most relevant feature.
##### Hyper-parameter tunning
Using RandomsearchCV in LG reg, KNN and XGboost for best results.
We have much improved the models. Although the accuracy of logestic regression found out to bethe heighest of 0.77. The accuracy of KNN found to be 0.72 with f1 score of 0.60which is also lower than Logestic regression. But the sensitivity was higher with value 0.80.Again we have 0.94 vaue of sensitivity for XGBoost. We will consider Logistic Regression as the best performing model among three. 
##### Hence using Logestic regression for further predictions

![download (3)](https://user-images.githubusercontent.com/64850346/112985015-41741c00-917d-11eb-8110-8bf4209c57b9.png)


Check the tableau dashboard for detail analysis:
 https://public.tableau.com/profile/ayan6555#!/vizhome/ds_capstone/overall_dashboard?publish=yes


