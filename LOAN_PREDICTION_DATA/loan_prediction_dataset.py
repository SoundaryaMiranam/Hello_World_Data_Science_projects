# -*- coding: utf-8 -*-
"""Loan_prediction_dataset

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BeVOBnUUxEBvbf5vaRtFyoGPsrCBpf6J

Data cleaning, data analysis, data visualization, machine learning and predict which of the customers will pay loan or not.

Introduction:

From the challange hosted at: https://datahack.analyticsvidhya.com/contest/practice-problem-loan-prediction-iii/

About Company:
Dream Housing Finance company deals in all home loans. They have presence across all urban, semi urban and rural areas. Customer first apply for home loan after that company validates the customer eligibility for loan.

Case:
Company wants to automate the loan eligibility process (real time) based on customer detail provided while filling online application form. These details are Gender, Marital Status, Education, Number of Dependents, Income, Loan Amount, Credit History and others. To automate this process, they have given a problem to identify the customers segments, those are eligible for loan amount so that they can specifically target these customers. Here they have provided a partial data set.

There are 2 data sets that are given. One is training data and one is testing data.The features in this dataset are as follows:

Loan ID  -  unique loan ID.

Gender - male or female.

Married - Applicant who is married is represented by Y and not married is represented as N.

Dependents - the number of people dependent on the applicant who has taken loan has been provided.

Education - It is either non -graduate or graduate.

Self_Employed - An applicant who is self employed is represented by Y and the one who is not is represented by N.

Applicant Income - The income of an Applicant.

Co-Applicant income - This represents the income of co-applicant.

Loan Amount - This amount represents the loan amount in thousands.

Loan_Amount_Term - This represents the number of months required to repay the loan.

Credit_History - A credit history is a record of a borrower’s responsible repayment of debts. It suggests → 1 denotes that the credit history is good and 0 otherwise.

Property_Area - The area where they belong to, here there are 3 types: Urban or Semi Urban or Rural.

Loan_Status - The applicant is eligible for loan it’s yes represented by Y else it’s no represented by N.

purpose:
The problem is to predict which of the customers will have their loan paid or not with given features.The variable Loan_Status is our target variable and the remaining are the feature variables of the dataset.


Exploratory Data Analysis:

Data cleaning:
columns which have missing values are:(Credit_History, Self_Employed, LoanAmount, Dependents, Loan_Amount_Term, Gender, Married).Imputed missing Values with sensible values.(most counts of value, mean, mode and median)
 
1. categorical columns - fill the missing values with most counts of value.(Credit_History, Self_Employed, Dependents, Gender, Married). 
2. numerical columns -  fill it with median, mode or most counts of value.(Loan_Amount_Term, LoanAmount).

Data visualization:

Univariate Analysis for loan prediction data:

1. Numerical Variables - Box plot
Applicant Income and LoanAmount has outliers in it.

Bivariate Analysis for loan prediction data:

1. categorical variables - count plot  
1) More males tend to take loan than females.

2) Married people are more on loan than unmarried people.

3) Self-employed people take less loans than those are not self-employed.

4) credit history shows that high number of people pay back their loans.

5) Semiurban obtain more loan, folowed by Urban and then rural.Which is understandable.

6) Most of the people opt for 360 cyclic loan term which is pay back within a year of time.   

7) Males generally have the highest income. Explicitly, Males that are married have greater income that unmarried male.

8) No one is dependent and a male tremendously has more income. 

9) A graduate who is a male has more income.

10) Not married and no one is dependent on such has more income. Also, Married and no one dependent has greater income with a decreasing effect as the dependents increases.

11) A graduate and married individual has more income.

12) Married and has a good credit history depicts more income. Also, Not married but has a good credit history follows in the hierarchy.

13) A graduate with no one dependent has more income.

14) Educated with good credit history depicts a good income. Also, not a graduate and have a good credit history can be traced to having a better income than a fellow with no degree

15) No one is dependent and self-employed has more income

16) A graduate but not self-employed has more income.

17) No one is dependent and have property in urban, rural and semiurban has more income.

2. Correlation matrix plot - 

No correlations are extremely high. The correlations between LoanAmount and ApplicantIncome can be explained.


Machine learning:

This is a supervised classification problem, as the target variable is categorical.
Here  logistic Regression works well to training set which gives 82.43 % accuracy.So we will use it to predict loan status on the test dataset.
"""

#https://www.kaggle.com/altruistdelhite04/loan-prediction-problem-dataset from

##loan prediction data science project
#https://medium.com/devcareers/loan-prediction-using-selected-machine-learning-algorithms-1bdc00717631
#https://www.codespeedy.com/loan-prediction-project-using-machine-learning-in-python/
#https://copycoding.com/d/machine-learning-project-in-python-to-predict-loan-approval-prediction-part-6-of-6- ---simple ML algo.
#https://github.com/shrikant-temburwar/Loan-Prediction-Dataset/blob/master/LoanPrediction.ipynb ----- all ML algo.



#https://www.kaggle.com/sowbarani/simple-eda-for-loan-prediction--- data transformation


#https://www.kaggle.com/ab9bhatia/complete-eda-for-loan-analysis
# VI. Univariate Analysis
# Continuous Variables
# In case of continuous variables, we need to understand the central tendency and spread of the variable.These are measured using various statistical metrics visualization methods such as Boxplot,Histogram/Distribution Plot, Violin Plot etc.

# Categorical Variables
# For categorical variables, we’ll use frequency table to understand distribution of each category. It can be be measured using two metrics, Count and Count% against each category. Countplot or Bar chart can be used as visualization.

# VII. Bivariate/Multivariate Analysis
# Bivariate/Multivariate Analysis finds out the relationship between two/two or more variables.We can perform Bivariate/Multivariate analysis for any combination of categorical and continuous variables. The combination can be: Categorical & Categorical, Categorical & Continuous and Continuous & Continuous.

#https://stackoverflow.com/questions/40901770/is-there-a-simple-way-to-change-a-column-of-yes-no-to-1-0-in-a-pandas-dataframe

#before describe cell


# NA_col = Loan_prediction_data.isnull().sum()
# NA_col = NA_col[NA_col.values >(0.3*len(Loan_prediction_data))]
# plt.figure(figsize=(20,4))
# NA_col.plot.bar()
# plt.title('List of Columns & NA counts where NA values are more than 30%')
# plt.show()

#import the files required
from google.colab import files
import io
uploaded =files.upload()
for fn in uploaded.keys():
   print('User uploaded file "{name}" with length {length} bytes'.format(name=fn, length=len(uploaded[fn])))

#import the files required
from google.colab import files
import io
upload =files.upload()
for fn in upload.keys():
   print('User uploaded file "{name}" with length {length} bytes'.format(name=fn, length=len(upload[fn])))

# Commented out IPython magic to ensure Python compatibility.
#Load the required libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

test_data = pd.read_csv('test_set.csv')
print("Rows, columns: " + str(test_data.shape))

Loan_prediction_data = pd.read_csv('train_set.csv')
print("Rows, columns: " + str(Loan_prediction_data.shape))

Loan_prediction_data.head()

Loan_prediction_data.dtypes

Loan_prediction_data.isnull().sum().sort_values(ascending = False)

missing = Loan_prediction_data.isnull().sum()
missing = missing[missing > 0]
missing.sort_values(inplace=True)
missing.plot.bar()
print("Number of attributes having missing values " + str(len(missing)))

Loan_prediction_data.describe()

"""#Data cleaning """

print(Loan_prediction_data['Gender'].value_counts())
Loan_prediction_data['Gender'].fillna('Male', inplace=True)

print(Loan_prediction_data['Married'].value_counts())
Loan_prediction_data['Married'].fillna('Yes', inplace=True)

print(Loan_prediction_data['Dependents'].value_counts())
Loan_prediction_data['Dependents'].fillna('0', inplace=True)

print(Loan_prediction_data['Self_Employed'].value_counts())
Loan_prediction_data['Self_Employed'].fillna('NO', inplace=True)

print(Loan_prediction_data['Credit_History'].value_counts())
Loan_prediction_data.Credit_History.fillna(1.0, inplace=True)

Loan_prediction_data.isnull().sum().sort_values(ascending = False)

print(Loan_prediction_data['Loan_Amount_Term'].value_counts())

print("Median of 'Loan_Amount_Term':",Loan_prediction_data['Loan_Amount_Term'].median())
print("Mode of 'Loan_Amount_Term':",Loan_prediction_data['Loan_Amount_Term'].mode())

Loan_prediction_data['Loan_Amount_Term'].fillna('360.0', inplace=True)

"""The most occurring value is 360 which is nothing but 30 years.There is no difference between median and mode values.Here it replaced with value (360.0). """

Loan_prediction_data["LoanAmount"] = Loan_prediction_data["LoanAmount"].replace(np.nan,Loan_prediction_data["LoanAmount"].mean())

Loan_prediction_data['LoanAmount'].hist(bins=50)
plt.show()

""" Loan_ID should be unique. So if there n number of rows, there should be n number of unique Loan_ID’s. Let us check for that. If there are any duplicate values we can remove that."""

Loan_prediction_data.apply(lambda x: len(x.unique()))

"""#Exploratory data analysis

1) Univariate Analysis

numercial data - box plot and histogram
"""

Loan_prediction_data.boxplot(column='ApplicantIncome')
plt.show()

Loan_prediction_data['ApplicantIncome'].hist(bins=50)
plt.show()

Loan_prediction_data['LoanAmount'].hist(bins=50)
plt.show()

Loan_prediction_data.boxplot(column='LoanAmount')
plt.show()

"""there are outliers in both the columns.

2) bivarient analysis

categorical data - count plot
"""

sns.countplot(y ='Gender' , hue = 'Loan_Status', data = Loan_prediction_data)
plt.show()

sns.countplot(y ='Married' , hue = 'Loan_Status', data = Loan_prediction_data)
plt.show()

sns.countplot(y ='Self_Employed' , hue = 'Loan_Status', data = Loan_prediction_data)
plt.show()

sns.countplot(y ='Credit_History' , hue = 'Loan_Status', data = Loan_prediction_data)
plt.show()

sns.countplot(y ='Property_Area' , hue = 'Loan_Status', data = Loan_prediction_data)
plt.show()

sns.countplot(y ='Loan_Amount_Term' , hue = 'Loan_Status', data = Loan_prediction_data)
plt.show()

"""1) More males tend to take loan than females.

2) Married people are more on loan than unmarried people.

3) Self-employed people take less loans than those are not self-employed.

4) credit history shows that high number of people pay back their loans.

5) Semiurban obtain more loan, folowed by Urban and then rural. This is logical!

6) Most of the people opt for 360 cyclic loan term which is pay back within a year of time.
"""

grid = sns.FacetGrid(Loan_prediction_data, row = 'Gender', col = 'Married', height = 3.5, aspect=1.8)
grid.map_dataframe(plt.hist, 'ApplicantIncome')
grid.set_axis_labels('ApplicantIncome', 'Count')
plt.show()

grid = sns.FacetGrid(Loan_prediction_data, row = 'Gender', col = 'Dependents', height = 3.5, aspect=1.8)
grid.map_dataframe(plt.hist, 'ApplicantIncome')
grid.set_axis_labels('ApplicantIncome', 'Count')
plt.show()

grid = sns.FacetGrid(Loan_prediction_data, row = 'Gender', col = 'Education', height = 3.5, aspect=1.8)
grid.map_dataframe(plt.hist, 'ApplicantIncome')
grid.set_axis_labels('ApplicantIncome', 'Count')
plt.show()

grid = sns.FacetGrid(Loan_prediction_data, row = 'Married', col = 'Dependents', height = 3.5, aspect=1.8)
grid.map_dataframe(plt.hist, 'ApplicantIncome')
grid.set_axis_labels('ApplicantIncome', 'Count')
plt.show()

grid = sns.FacetGrid(Loan_prediction_data, row = 'Married', col = 'Education', height = 3.5, aspect=1.8)
grid.map_dataframe(plt.hist, 'ApplicantIncome')
grid.set_axis_labels('ApplicantIncome', 'Count')
plt.show()

grid = sns.FacetGrid(Loan_prediction_data, row = 'Married', col = 'Credit_History', height = 3.5, aspect=1.8)
grid.map_dataframe(plt.hist, 'ApplicantIncome')
grid.set_axis_labels('ApplicantIncome', 'Count')
plt.show()

grid = sns.FacetGrid(Loan_prediction_data, row = 'Education', col = 'Dependents', height = 3.5, aspect=1.8)
grid.map_dataframe(plt.hist, 'ApplicantIncome')
grid.set_axis_labels('ApplicantIncome', 'Count')
plt.show()

grid = sns.FacetGrid(Loan_prediction_data, row = 'Education', col = 'Credit_History', height = 3.5, aspect=1.8)
grid.map_dataframe(plt.hist, 'ApplicantIncome')
grid.set_axis_labels('ApplicantIncome', 'Count')
plt.show()

grid = sns.FacetGrid(Loan_prediction_data, row = 'Self_Employed', col = 'Dependents', height = 3.5, aspect=1.8)
grid.map_dataframe(plt.hist, 'ApplicantIncome')
grid.set_axis_labels('ApplicantIncome', 'Count')
plt.show()

grid = sns.FacetGrid(Loan_prediction_data, row = 'Self_Employed', col = 'Education', height = 3.5, aspect=1.8)
grid.map_dataframe(plt.hist, 'ApplicantIncome')
grid.set_axis_labels('ApplicantIncome', 'Count')
plt.show()

grid = sns.FacetGrid(Loan_prediction_data, row = 'Property_Area', col = 'Dependents', height = 3.5, aspect=1.8)
grid.map_dataframe(plt.hist, 'ApplicantIncome')
grid.set_axis_labels('ApplicantIncome', 'Count')
plt.show()

"""1. Males generally have the highest income. Explicitly, Males that are married have greater income that unmarried male.
2. No one is dependent and a male tremendously has more income. 
3. A graduate who is a male has more income.
4. Not married and no one is dependent on such has more income. Also, Married and no one dependent has greater income with a decreasing effect as the dependents increases.
5. A graduate and married individual has more income.
6. Married and has a good credit history depicts more income. Also, Not married but has a good credit history follows in the hierarchy.
7. A graduate with no one dependent has more income.
8. Educated with good credit history depicts a good income. Also, not a graduate and have a good credit history can be traced to having a better income than a fellow with no degree
9. No one is dependent and self-employed has more income
10. A graduate but not self-employed has more income.
11. No one is dependent and have property in urban, rural and semiurban has more income.

Correlation matrix plot
"""

sns.heatmap(Loan_prediction_data.corr())
plt.show()

"""#Machine learning"""

#drop all the object types features
Loan_prediction_data = Loan_prediction_data.drop(['Loan_ID'], axis=1)

Loan_prediction_data.columns

from sklearn.preprocessing import LabelEncoder
 var_mod = ['Gender','Married','Dependents','Education','Self_Employed','Property_Area','Loan_Status']
 le = LabelEncoder()
 for i in var_mod:
     Loan_prediction_data[i] = le.fit_transform(Loan_prediction_data[i])
 Loan_prediction_data.dtypes

# Splitting traing data
X = Loan_prediction_data.drop('Loan_Status', axis=1)
y = Loan_prediction_data.Loan_Status

X

y

test_data.isnull().sum().sort_values(ascending = False)

print(test_data['Gender'].value_counts())
test_data['Gender'].fillna('Male', inplace=True)

print(test_data['Dependents'].value_counts())
test_data['Dependents'].fillna('0', inplace=True)

print(test_data['Self_Employed'].value_counts())
test_data['Self_Employed'].fillna('NO', inplace=True)

print(test_data['Credit_History'].value_counts())
test_data.Credit_History.fillna(1.0, inplace=True)

print(test_data['Loan_Amount_Term'].value_counts())

print("Median of 'Loan_Amount_Term':",test_data['Loan_Amount_Term'].median())
print("Mode of 'Loan_Amount_Term':",test_data['Loan_Amount_Term'].mode())

test_data['Loan_Amount_Term'].fillna('360.0', inplace=True)

test_data["LoanAmount"] = test_data["LoanAmount"].replace(np.nan,test_data["LoanAmount"].mean())

test = test_data.drop(['Loan_ID'], axis=1)

var_mod = ['Gender','Married','Dependents','Education','Self_Employed','Property_Area']
 le = LabelEncoder()
 for i in var_mod:
     test[i] = le.fit_transform(test[i])
 test.dtypes

# Splitting the dataset into the Training set and Test set
 from sklearn.model_selection import train_test_split
 X_train, X_val, y_train, y_val = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_val = sc.fit_transform(X_val)

# Fitting LogisticRegression to the Training set
from sklearn.linear_model import LogisticRegression
LR_classifier = LogisticRegression(random_state = 0)
LR_classifier.fit(X_train, y_train)
y_pred = LR_classifier.predict(X_val)

# Measuring Accuracy
from sklearn import metrics
print('The accuracy of Logistic Regression is: ', metrics.accuracy_score(y_pred, y_val))

# Fitting K-NN to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_val)

# Measuring Accuracy
from sklearn import metrics
print('The accuracy of KNN is: ', metrics.accuracy_score(y_pred, y_val))

# Fitting SVM to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_val)

# Measuring Accuracy
from sklearn import metrics
print('The accuracy of SVM is: ', metrics.accuracy_score(y_pred, y_val))

# Fitting Decision Tree Classification to the Training set
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_val)

# Measuring Accuracy
from sklearn import metrics
print('The accuracy of Decision Tree Classifier is: ', metrics.accuracy_score(y_pred, y_val))

# Fitting Random Forest Classification to the Training set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_val)

# Measuring Accuracy
from sklearn import metrics
print('The accuracy of Random Forest Classification is: ', metrics.accuracy_score(y_pred, y_val))

"""Training dataset results:

The accuracy of Logistic Regression is: 82.43 %

The accuracy of KNN is: 79.51 %

The accuracy of SVM is: 81.95 %

The accuracy of Decision Tree Classifier is: 72.19 %

The accuracy of Random Forest Classification is: 78.53 %

#Testing
"""

# predict on new set with logistic regression
prediction = LR_classifier.predict(test)

test_data['Loan_Status_Prediction'] = prediction 
test_data['Loan_Status_Prediction'] = test_data['Loan_Status_Prediction'].map({1: 'Yes', 0: 'No'})
test_data.head(10)