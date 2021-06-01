# -*- coding: utf-8 -*-
"""Boston_housing_data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B2xRhPtQJJsZFF_ICIIJEbsHlAkiuIuR
"""



"""
Introduction:

The Boston Housing Dataset is a derived from information collected by the U.S. Census Service concerning housing in the area of Boston MA. The following describes the dataset columns:

CRIM - per capita crime rate by town

ZN - proportion of residential land zoned for lots over 25,000 sq.ft.

INDUS - proportion of non-retail business acres per town.

CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)

NOX - nitric oxides concentration (parts per 10 million)

RM - average number of rooms per dwelling

AGE - proportion of owner-occupied units built prior to 1940

DIS - weighted distances to five Boston employment centres

RAD - index of accessibility to radial highways

TAX - full-value property-tax rate per $10,000

PTRATIO - pupil-teacher ratio by town

B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town

LSTAT - % lower status of the population

MEDV - Median value of owner-occupied homes in $1000'

purpose:

The objective is to predict the value of prices of the house using the given features.The prices of the house indicated by the variable MEDV is our target variable and the remaining are the feature variables of a house dataset.

Exploratory Data Analysis:

There two variables cloumns which are:
1)Categorical variables: Bar plot('TAX','RAD','CHAS(after processing)')
2)Continuous variables: Histogram('CRIM', 'ZN', 'INDUS', 'NOX', 'RM', 'AGE', 'DIS', 'PTRATIO', 'B', 'LSTAT')

Box plot for Boston housing data:
CRIM has outliers in it which lies beyond point 40.
Most of the columns are skewed except 'RM' weather it be numeric or non-numeric.

Correlation matrix plot for Boston housing data:
1.  RM has a strong positive correlation with PRICE where as LSTAT has a high negative correlation with PRICE.
2.  The features RAD, TAX have a correlation of 0.91. These feature pairs are strongly correlated to each other.
3. The features DIS and AGE also have a strong correlation of -0.75.
4. CRIM is strongly associated with variables RAD and TAX.
5. INDUS is strongly correlated with NOX ,which shows that industrial areas has nitrogen oxides concentration.

Additional points:

 1)Population of lower status increases/decreases with decrease/increase in price.

 2)As Crime rate increases the rate of House decreases.

 3)As Nitric Oxide concentration increases the rate of House decreases.

Specifically, there are also missing observations for some columns.
Imputed missing Values with sensible values.(mean and median)


Machine learning:

Based on the problem statement we need to create a supervised ML Regression model, as the target variable is Continuous.
Here we linear regression is applied which gives 65% accuracy.So, the prepared model is not very good for predicting the housing prices.

Regressor model performance:
Mean absolute error(MAE) = 3.15
Mean squared error(MSE) = 25.11
Median absolute error = 2.25
Explain variance score = 0.66
R2 score = 0.66










"""

#boston housing dataset in:notebooks
#purpose:given a set of features that describe a house in Boston, our machine learning model must predict the house price.


#https://analyticsindiamag.com/5-ways-handle-missing-values-machine-learning-datasets/
#https://www.kaggle.com/dansbecker/handling-missing-values - - for better words
#https://machinelearningmastery.com/handle-missing-data-python/ --imputation types and algo which support missing values


#housing_data["LSTAT"] = housing_data["LSTAT"].replace(np.nan,housing_data["LSTAT"].mean())
#housing_data['AGE'].replace(np.NaN , housing_data['AGE'].mean() , inplace=True)

##housing_data.dropna(inplace = True)
#print("Rows, columns: " + str(housing_data.shape))
#housing_data.isnull().sum()

#https://stackoverflow.com/questions/51293196/attributeerror-numpy-ndarray-object-has-no-attribute-drop
#from sklearn.preprocessing import StandardScaler
#sc = StandardScaler()
# = sc.fit_transform(housing_data)

#https://thinkingneuron.com/boston-housing-price-prediction-case-study-in-python/ -- data exploration (catagorical and continuous)
#https://towardsdatascience.com/linear-regression-on-boston-housing-dataset-f409b7e4a155--- 

#https://thinkingneuron.com/boston-housing-price-prediction-case-study-in-python/


#https://stackoverflow.com/questions/41925157/logisticregression-unknown-label-type-continuous-using-sklearn-in-python ----understand about regression and classification

##other way to do it 

#plt.hist(boston_df.NOX)
#plt.xlabel("Nitric oxides concentration (parts per 10 million)")
#plt.ylabel("Frequency")
#plt.title("NOX")
#plt.show()

#https://geeksgod.com/exploratory-data-analysis-of-boston-housing-dataset/

#Plotting graph between NOX and MEDV

# plt.bar(housing_data.NOX,housing_data.PRICE)
# plt.xlabel('Nitric Oxide concentration')
# plt.ylabel('Price of the House')
# plt.title('Nitric Oxide concentration vs Price of house')
# plt.plot()
# #As Nitric Oxide concentration increases the rate of House decreases

# #Plotting graph between LSTAT and MEDV

# plt.bar(housing_data.LSTAT,housing_data.PRICE)
# plt.xlabel('% lower status population')
# plt.ylabel('Price of the House')
# plt.title('% lower status population vs Price of house')
# plt.plot()
# #percentage lower status population is low, price of houses are high

# plt.bar(housing_data.CRIM,housing_data.PRICE)
# plt.xlabel('Crime Rate')
# plt.ylabel('Price of the House')
# plt.title('Crime rate vs Price of house')
# plt.plot()
# #As Crime rate increases the rate of House decreases

#https://vitalflux.com/pandas-impute-missing-values-mean-median-mode/ --- when to use mean ,median and mode.

#https://analyticsindiamag.com/top-6-regression-algorithms-used-data-mining-applications-industry/
#https://www.tutorialspoint.com/machine_learning_with_python/machine_learning_with_python_regression_algorithms_overview.htm
#https://www.tutorialspoint.com/machine_learning_with_python/regression_algorithms_linear_regression.htm

#import the files required
from google.colab import files
import io
uploaded =files.upload()
for fn in uploaded.keys():
   print('User uploaded file "{name}" with length {length} bytes'.format(name=fn, length=len(uploaded[fn])))

# Commented out IPython magic to ensure Python compatibility.
#Load the required libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

#read the data from the file
housing_data = pd.read_csv('HousingData.csv')
print("Rows, columns: " + str(housing_data.shape))

housing_data.sample(10)

"""#Statistical analysis"""

housing_data.dtypes

housing_data.isnull().sum()

"""We can see that there are columns that have missing values which are 'CRIM', 'ZN', 'INDUS', 'CHAS', 'AGE', 'LSTAT'."""

housing_data.describe()

housing_data.rename(columns={'MEDV':'PRICE'}, inplace=True)

"""#Box plot for Boston housing data

Here we can see that the variables ‘chas’, 'TAX' and ‘rad’ are non numeric others are numeric.
"""

fig = plt.figure(figsize=(40,5))
features = ["TAX","RAD","CHAS"]
for i in range(3):
    ax1 = fig.add_subplot(1,3,i+1)
    sns.countplot(x=features[i],data=housing_data)

"""As you can see CHAS is skewed.There is just one bar which is dominating and other one have very less rows. """

housing_data.hist(['CRIM', 'ZN', 'INDUS', 'NOX', 'RM', 'AGE', 'DIS', 'PTRATIO', 'B', 'LSTAT'], figsize=(18,15))
plt.show()

"""CRIM has outliers in it beyond point 40.

#Correlation matrix for Boston housing data
"""

corr = housing_data.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(corr, annot=True, vmin=-1.0, vmax=1.0)
plt.show()

"""1.  RM has a strong positive correlation with PRICE where as LSTAT has a high negative correlation with PRICE.
2.  The features RAD, TAX have a correlation of 0.91. These feature pairs are strongly correlated to each other.
3. The features DIS and AGE also have a strong correlation of -0.75.
4. CRIM is strongly associated with variables RAD and TAX.
5. INDUS is strongly correlated with NOX ,which shows that industrial areas has nitrogen oxides concentration.
"""

sns.regplot(y="PRICE",x="LSTAT", data=housing_data, fit_reg= True)
plt.title("Relationship between Lower Status Population and Price")
plt.show()

sns.regplot(y="PRICE",x="CRIM", data=housing_data, fit_reg= True)
plt.title("Relationship between Crime rate and Price")
plt.show()

sns.regplot(y="PRICE",x="NOX", data=housing_data, fit_reg= True)
plt.title("Relationship between Nitric Oxide concentration and Price")
plt.show()

"""1)We can see a strong negative correlation between lower status population and price.
2)As Crime rate increases the rate of House decreases.
3)As Nitric Oxide concentration increases the rate of House decreases.

#Feature Selection for Boston housing data
"""

correlations = housing_data.corr()['PRICE'].sort_values(ascending=False)
correlations.plot(kind='bar')

print(correlations)

print(abs(correlations) >= 0.40)

"""These featurs are effecting the target variable:
'RM', 'NOX', 'TAX', 'INDUS', 'PTRATIO', 'LSTAT'.

#Handling missing values of Boston housing data
"""

housing_data["CRIM"] = housing_data["CRIM"].replace(np.nan,housing_data["CRIM"].median())
housing_data["ZN"] = housing_data["ZN"].replace(np.nan,housing_data["ZN"].median())
housing_data["INDUS"] = housing_data["INDUS"].replace(np.nan,housing_data["INDUS"].mean()) 
housing_data["CHAS"] = housing_data["CHAS"].replace(np.nan,housing_data["CHAS"].median())
housing_data["AGE"] = housing_data["AGE"].replace(np.nan,housing_data["AGE"].median())
housing_data["LSTAT"] = housing_data["LSTAT"].replace(np.nan,housing_data["LSTAT"].median())

#housing_data.CHAS = housing_data.CHAS.astype(int)

"""#Machine learning"""

from sklearn.model_selection import train_test_split, cross_val_score
X = housing_data.drop('PRICE',axis = 1)
Y = housing_data['PRICE']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

from sklearn.linear_model import LinearRegression
import sklearn.metrics as sm
from sklearn import linear_model, metrics
regressor = LinearRegression()
regressor.fit(X_train,Y_train)
regressor_predict = regressor.predict(X_test)
accuracy = regressor.score(X_test,Y_test)
print('Accuracy of the model:',accuracy*100,'%' )

print("Regressor model performance:")
print("Mean absolute error(MAE) =", (round(sm.mean_absolute_error(Y_test, regressor_predict), 2)))
print("Mean squared error(MSE) =", (round(sm.mean_squared_error(Y_test, regressor_predict), 2)))
print("Median absolute error =", (round(sm.median_absolute_error(Y_test, regressor_predict), 2)))
print("Explain variance score =",( round(sm.explained_variance_score(Y_test, regressor_predict), 2)))
print("R2 score =", (round(sm.r2_score(Y_test, regressor_predict), 2)))

plt.style.use('fivethirtyeight')
plt.scatter(regressor.predict(X_train), regressor.predict(X_train) - Y_train, color = "green", s = 20, label = 'Train data')
plt.scatter(regressor.predict(X_test), regressor.predict(X_test) - Y_test, color = "blue", s = 20, label = 'Test data')
plt.hlines(y = 0, xmin = 0, xmax = 50, linewidth = 2)
plt.legend(loc = 'upper right')
plt.title("Residual errors")
plt.show()