
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

df = pd.read_csv('earthquake_1995-2023.csv')
df.head()

df.shape

df.info()

pd.set_option('display.max_columns',None)
df.head()

df.drop(['cdi','mmi','tsunami','sig','net','nst','dmin','gap','title','magType','continent','country'],
        axis=1,inplace=True)

df.info()

df.describe()

splitted = df['date_time'].str.split(' ', n=1,
									expand=True)

df['Date'] = splitted[0]
df['Time'] = splitted[1].str[:]

df.drop('date_time',
        axis=1,
        inplace=True)
df.head()

df.shape

splitted = df['Date'].str.split('-', expand=True)

df['day'] = splitted[0].astype('int')
df['month'] = splitted[1].astype('int')
df['year'] = splitted[2].astype('int')

df.drop('Date', axis=1,
        inplace=True)
df.head()

df.info()

# depth per passing year

plt.figure(figsize=(10, 5))
x = df.groupby('year').mean()['depth']
x.plot.bar()
plt.show()

plt.figure(figsize=(10, 5))
x = df.groupby('alert').mean()['depth']
x.plot.bar()
plt.show()

#changes of magnitude with months
# here magnitude is higher b/w month(4) and month(6)
# and sharpdrop b/w month(8) and month(10)

plt.figure(figsize=(10, 5))
sns.lineplot(data=df,
			x='month',
			y='magnitude')
plt.show()

plt.subplots(figsize=(15, 5))

plt.subplot(1, 2, 1)
sns.distplot(df['depth'])

plt.subplot(1, 2, 2)
sns.boxplot(df['depth'])

plt.show()

plt.subplots(figsize=(15, 5))

plt.subplot(1, 2, 1)
sns.distplot(df['magnitude'])

plt.subplot(1, 2, 2)
sns.boxplot(df['magnitude'])

plt.show()

plt.figure(figsize=(10, 8))
sns.scatterplot(data=df,
			x='latitude',
			y='longitude',
			hue='magnitude')
plt.show()

import plotly.express as px
import pandas as pd

fig = px.scatter_geo(df, lat='latitude',
					lon='longitude',
					color="magnitude",
					fitbounds='locations',
					scope='world')
fig.show()

obj = (df.dtypes == 'object')
print("Categorical variables:",len(list(obj[obj].index)))

from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
df['Time'] = label_encoder.fit_transform(df['Time'])

from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
df['location'] = label_encoder.fit_transform(df['location'])

obj = (df.dtypes == 'object')
print("Categorical variables:",len(list(obj[obj].index)))

plt.figure(figsize=(12,6))

sns.heatmap(df.corr(),cmap='BrBG',fmt='.2f',
            linewidths=2,annot=True)

for col in df.columns:
 df[col] = df[col].fillna('No Alert')

df.isna().sum()

df.head()

X = df.drop(['alert'],axis=1)
Y = df[['alert']]
X.shape,Y.shape

X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
                                                    test_size=0.4,
                                                    random_state=42)
X_train.shape, X_test.shape, Y_train.shape, Y_test.shape

#from sklearn.svm import SVR
from sklearn.ensemble import RandomForestClassifier
#from sklearn.multioutput import MultiOutputRegressor

#classifier = MultiOutputRegressor(LinearRegression())
classifier = RandomForestClassifier()
classifier.fit(X_train, Y_train)

predictions = classifier.predict(X_test)
print(predictions)

predictions = classifier.predict([[6.5,	192.955,	-13.8814,	167.1580,	427,	365,	16,	8,	2023]])
predictions

print('alert level :',predictions[0])

"""### Alert with magnitude"""

import pandas as pd

df_1 = pd.read_csv('/content/earthquake-mag-depth-alert.csv')
df_1.head()

for col in df_1.columns:
 df_1[col] = df_1[col].fillna('No Alert')

df_1.isna().sum()

from sklearn.model_selection import train_test_split

x = df_1.drop(['alert'],axis=1)
y = df_1[['alert']]
x.shape,y.shape

x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                    test_size=0.3,
                                                    random_state=42)
x_train.shape, x_test.shape, y_train.shape, y_test.shape

df_1.head()

from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier()
forest.fit(x, y)

predictions = forest.predict(x_test)
print(predictions)

m = input('Enter Eartquake Magnitude: ')
d = input('Enter Earthquake Depth: ')
i = [m,d]

predictions = forest.predict([i])
print('Alert Level: ', predictions[0])
