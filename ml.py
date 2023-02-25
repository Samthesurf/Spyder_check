import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


np.random.seed(42)

plt.rc('font', size=12)
plt.rc('axes', labelsize=14, titlesize=14)
plt.rc('legend', fontsize=12)
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)

# Download and prepare the data
data_root = "https://github.com/ageron/data/raw/main/"
life_sat = pd.read_csv(data_root+'lifesat/lifesat.csv')
life_sat.columns = life_sat.columns.str.replace(' ,', '')
X = life_sat[["GDP per capita (USD)"]].values
Y = life_sat[["Life satisfaction"]].values
# Data visualization
life_sat.plot(kind='scatter', grid=True, x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23_500, 62_500, 4, 9])
plt.show()
# select a linear model
model = LinearRegression()
# training time
model.fit(X, Y)
# make a new prediction
X_new = [[37_655.2]]
print(model.predict(X_new))
