#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import seaborn as sns


#importing dataset
car_dataset = pd.read_csv('C:/Python/Python_Upgrad/LinearRegression/CarPrice_Assignment.csv')

#Handling missing data
car_dataset.info()

#Checking data
pd.set_option('display.max_columns', None)
car_dataset.head()

car_dataset['CarName'] = car_dataset['CarName'].str.split(' ',expand=True)
car_dataset.rename(columns = {'CarName' : 'CarCompany'},inplace=True)
car_dataset.head(5)

#car_ID is not going to add any value in model preparation so lets drop these two columns
car_dataset.drop('car_ID',1,inplace=True)


#Checking Unique Car names
car_dataset['CarCompany'].unique()
#Here we can see few spelling mistakes of upper case lower case 
#issues in company names extracted. Let's correct these
car_dataset['CarCompany'] = car_dataset['CarCompany'].str.replace('maxda', 'mazda')
car_dataset['CarCompany'] = car_dataset['CarCompany'].str.replace('Nissan', 'nissan')
car_dataset['CarCompany'] = car_dataset['CarCompany'].str.replace('porcshce', 'porsche')
car_dataset['CarCompany'] = car_dataset['CarCompany'].str.replace('toyouta', 'toyota')
car_dataset['CarCompany'] = car_dataset['CarCompany'].str.replace('vokswagen', 'volkswagen')
car_dataset['CarCompany'] = car_dataset['CarCompany'].str.replace('vw', 'volkswagen')

car_dataset['CarCompany'].unique()

#Splitting dependent and independent variables
sns.pairplot(car_dataset)
#plt.show()

'''Now lets see the association with categorical variables

 1.  CarCompany
 2.  fueltype
 3.  aspiration
 4.  doornumber
 5.  carbody
 6.  drivewheel
 10.  enginelocation
 11.  enginetype
 12.  cylindernumber
 13.  fuelsystem
 '''

# lets define a function to plot price across categorical variables
def plot_cat(cat_var):
    plt.figure(figsize=(150,30))
    plt.subplot(2,5,1)
    sns.boxplot(x=cat_var, y='price', data=car_dataset)
    plt.show()
	
#Car company vs price
plot_cat('CarCompany')

#Car fueltype vs price
plot_cat('fueltype')
#Car aspiration vs price
plot_cat('aspiration')
#Car doornumber vs price
plot_cat('doornumber')
#Car carbody vs price
plot_cat('carbody')

#Car drivewheel vs price
plot_cat('drivewheel')
#Car enginelocation vs price
plot_cat('enginelocation')
#Car enginetype vs price
plot_cat('enginetype')
#Car cylindernumber vs price
plot_cat('cylindernumber')

#Car fuelsystem vs price
plot_cat('fuelsystem')

#Taking Car_dataset from car_dataset
car_dataset  = car_dataset




