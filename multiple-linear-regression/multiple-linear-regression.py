import numpy as np import matplotlib.pyplot as pltimport pandas as pd#import statsmodels.formula.api as smfrom sklearn.model_selection import train_test_splitfrom sklearn.preprocessing import LabelEncoder, OneHotEncoderfrom sklearn.compose import ColumnTransformerfrom sklearn.linear_model import LinearRegressiondataset = pd.read_csv('50-startups-data.csv');X = dataset.iloc[:,:-1].valuesy = dataset.iloc[:,4].valueslabelencoder_X = LabelEncoder()X[:,3] = labelencoder_X.fit_transform(X[:,3])ct = ColumnTransformer([('encoder', OneHotEncoder(), [3])], remainder='passthrough')X = np.array(ct.fit_transform(X), dtype=np.float)# Avoid dummy variable trapX = X[:, 1:]X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)regressor = LinearRegression()regressor.fit(X_train, y_train)y_pred = regressor.predict(X_test)X = np.append( arr = np.ones((50, 1)).astype(int), values = X, axis = 1)