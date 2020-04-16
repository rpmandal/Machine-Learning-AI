# Supress Warnings
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd

CarPrice = pd.read_csv('C:/Python/Python_Upgrad/LinearRegression/CarPrice_Assignment.csv')

# Dataset Analysis
"""
CarPrice.head()
CarPrice.shape
CarPrice.info()
CarPricedescribe = CarPrice.describe()
import matplotlib.pyplot as plt
import seaborn as sns
sns.pairplot(CarPrice)
plt.show()
CarPrice.CarName.nunique()
"""


# Extract brand name from CarName
CarPrice['Brand'] = CarPrice.CarName.apply(lambda x: x.lower().split()[0])

# Removed car_ID and CarName as many uniqueid not required
NewCarPrice = CarPrice.drop(['car_ID','CarName'], axis=1)


NewCarPrice['Brand'] = NewCarPrice['Brand'].str.replace('maxda', 'mazda')
NewCarPrice['Brand'] = NewCarPrice['Brand'].str.replace('porcshce', 'porsche')
NewCarPrice['Brand'] = NewCarPrice['Brand'].str.replace('toyouta', 'toyota')
NewCarPrice['Brand'] = NewCarPrice['Brand'].str.replace('vokswagen', 'volkswagen')
NewCarPrice['Brand'] = NewCarPrice['Brand'].str.replace('vw', 'volkswagen')



# Divided dataset into Dependent and Independent variable
X = NewCarPrice.iloc[:, [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24]].values
y = NewCarPrice.iloc[:, [23]].values
df_X = pd.DataFrame(X)
df_y = pd.DataFrame(y)


# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 1] = labelencoder.fit_transform(X[:, 1]) # change text into number
X[:, 2] = labelencoder.fit_transform(X[:, 2]) # change text into number
X[:, 3] = labelencoder.fit_transform(X[:, 3]) # change text into number
X[:, 4] = labelencoder.fit_transform(X[:, 4]) # change text into number
X[:, 5] = labelencoder.fit_transform(X[:, 5]) # change text into number
X[:, 6] = labelencoder.fit_transform(X[:, 6]) # change text into number
X[:, 12] = labelencoder.fit_transform(X[:, 12]) # change text into number
X[:, 13] = labelencoder.fit_transform(X[:, 13]) # change text into number
X[:, 15] = labelencoder.fit_transform(X[:, 15]) # change text into number
X[:, 23] = labelencoder.fit_transform(X[:, 23]) # change text into number



# Converting dummy variable of carbody
onehotencoder = OneHotEncoder(categorical_features = [4])
X = onehotencoder.fit_transform(X).toarray()
# Avoiding the Dummy Variable Trap
X = X[:, 1:]

# Converting dummy variable of drivewheel
onehotencoder = OneHotEncoder(categorical_features = [8])
X = onehotencoder.fit_transform(X).toarray()
# Avoiding the Dummy Variable Trap
X = X[:, 1:]

# Converting dummy variable of cylindernumber
onehotencoder = OneHotEncoder(categorical_features = [17])
X = onehotencoder.fit_transform(X).toarray()
# Avoiding the Dummy Variable Trap
X = X[:, 1:]

# Converting dummy variable of enginetype
onehotencoder = OneHotEncoder(categorical_features = [22])
X = onehotencoder.fit_transform(X).toarray()
# Avoiding the Dummy Variable Trap
X = X[:, 1:]

# Converting dummy variable of fuelsystem
onehotencoder = OneHotEncoder(categorical_features = [29])
X = onehotencoder.fit_transform(X).toarray()
# Avoiding the Dummy Variable Trap
X = X[:, 1:]

# Converting dummy variable of Brand
onehotencoder = OneHotEncoder(categorical_features = [43])
X = onehotencoder.fit_transform(X).toarray()
# Avoiding the Dummy Variable Trap
X = X[:, 1:]


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection  import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)



# Building the optimal model using Backward Elimination
import statsmodels.formula.api as sm
X = np.append(arr = np.ones((205, 1)).astype(int), values = X, axis = 1)
X_opt = X[:, :]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()
"""
If P value is above significance level (0.05) delete that column one by one,
taking highest P value column out first 
"""

X_opt = X[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,23,24,25,26,27,28,29,30,
          31,32,33,34,35,36,37,38,39,40,
          41,42,43,44,45,46,47,48,49,50,
          51,52,53,54,55,56,57,58,59,60,
          61,62,64]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,23,24,25,26,27,28,29,30,
          31,32,33,34,35,36,37,38,39,40,
          42,43,44,45,46,47,48,49,50,
          51,52,53,54,55,56,57,58,59,60,
          61,62,63]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,23,24,26,27,28,29,30,
          31,32,33,34,35,36,37,38,39,40,
          41,42,43,44,45,46,47,48,49,50,
          51,52,53,54,55,56,57,58,59,60,
          61,62]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,23,24,25,26,27,28,29,30,
          31,32,33,34,35,36,37,38,39,40,
          41,42,43,44,45,46,47,48,49,50,
          51,52,53,54,55,56,57,58,60,
          61]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,24,25,26,27,28,29,30,
          31,32,33,34,35,36,37,38,39,40,
          41,42,43,44,45,46,47,48,49,50,
          51,52,53,54,55,56,57,58,59,60]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,23,24,25,26,27,28,29,30,
          31,32,33,34,35,36,37,38,39,40,
          41,42,43,44,45,46,47,48,49,50,
          51,52,53,54,55,56,57,58,59]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,23,24,25,26,28,29,30,
          31,32,33,34,35,36,37,38,39,40,
          41,42,43,44,45,46,47,48,49,50,
          51,52,53,54,55,56,57,58]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,23,24,25,26,27,28,29,30,
          31,32,33,34,35,36,37,38,39,40,
          41,42,43,44,46,47,48,49,50,
          51,52,53,54,55,56,57]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,23,24,25,26,27,28,29,30,
          31,32,33,34,35,36,37,38,39,40,
          41,42,43,44,45,46,47,48,49,50,
          51,52,53,54,55,56]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,24,25,26,27,28,29,30,
          31,32,33,34,35,36,37,38,39,40,
          41,42,43,44,45,46,47,48,49,50,
          51,52,53,54,55]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,17,18,19,20,
          21,22,23,24,25,26,27,28,29,30,
          31,32,33,34,35,36,37,38,39,40,
          41,42,43,44,45,46,47,48,49,50,
          51,52,53,54]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,23,24,25,26,27,28,29,30,
          31,32,33,35,36,37,38,39,40,
          41,42,43,44,45,46,47,48,49,50,
          51,52,53]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,23,24,25,26,27,28,29,30,
          31,32,33,34,35,36,37,38,39,40,
          41,42,43,44,45,46,47,48,49,50,
          51,52]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,23,24,25,26,27,28,29,30,
          31,32,33,34,35,36,37,38,39,40,
          41,42,43,44,45,46,47,48,49,50,
          51]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,23,24,25,26,27,28,29,30,
          31,32,33,34,35,37,38,39,40,
          41,42,43,44,45,46,47,48,49,50]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,23,24,25,26,27,28,30,
          31,32,33,34,35,36,37,38,39,40,
          41,42,43,44,45,46,47,48,49]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,23,24,26,27,28,29,30,
          31,32,33,34,35,36,37,38,39,40,
          41,42,43,44,45,46,47,48]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,23,24,25,26,27,28,30,
          31,32,33,34,35,36,37,38,39,40,
          41,42,43,44,45,46,47]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,23,24,25,26,27,28,29,30,
          31,32,33,34,35,36,37,38,39,40,
          41,42,43,44,45,46]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,23,24,25,26,28,29,30,
          31,32,33,34,35,36,37,38,39,40,
          41,42,43,44,45]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,23,24,25,26,27,28,29,30,
          31,32,33,34,35,36,37,38,39,40,
          42,43,44]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,
          21,22,23,24,25,26,27,28,29,30,
          31,32,33,34,35,36,37,38,39,40,
          41,42,43]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,23,24,25,26,27,28,29,30,
          31,32,33,34,35,36,37,38,39,40,
          41,42]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,18,19,20,
          21,22,23,24,25,26,27,28,29,30,
          31,32,33,34,35,36,37,38,39,40,
          41]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,19,20,
          21,22,23,24,25,26,27,28,29,30,
          31,32,33,34,35,36,37,38,39,40]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,23,24,25,26,27,28,29,30,
          31,32,33,34,35,36,37,38]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,23,24,25,26,27,29,30,
          31,32,33,34,35,36,37,38]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,24,25,26,27,28,29,30,
          31,32,33,34,35,36,37]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,23,25,26,27,28,29,30,
          31,32,33,34,35,36]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,23,25,26,27,28,29,30,
          31,32,33,34,35]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,13,14,15,16,17,18,19,20,
          21,22,23,24,25,26,27,28,29,30,
          31,32,33,34]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,23,24,26,27,28,29,30,
          31,32,33]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X_opt[:, [0,1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,17,18,19,20,
          21,22,23,24,25,26,27,28,29,30,
          31,32]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

"""
Now the P value of all cofficent is less then significance level (0.05). 
Now we need to stop backward elemination.
Final values of R-squared and Adj. R-squared
R-squared:                       0.958
Adj. R-squared:                  0.950
"""

from sklearn.metrics import r2_score
r2_score(y_test,y_pred)
# 0.8771661137689065










