# Linear Regression
# Logistic Regression
# Decision Tree
# Random Forest
# K nearest neighbours
# K means Clustering
# Support Vector Machines
# Naive Bayes Classification

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

companies = pd.read_csv('1000_Companies.csv')

x = companies.iloc[:, 0:-1].values
y = companies.iloc[:, 4].values

print(companies.head())