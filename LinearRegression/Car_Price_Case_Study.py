# -*- coding: utf-8 -*-
"""
Created on 25-May-2019

@author: Rana Pratap Mandal
"""

#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing dataset
df = pd.read_csv('C:/Python/Python_Upgrad/LinearRegression/CarPrice_Assignment.csv')

'''
Data Pre processing
'''
#Handling missing data
df.info()
#from dataset info we can see there is no missing data.
x = df.iloc[:,:-1].values  
y = df.iloc[:,-1:].values

#From info we can see there is no 

