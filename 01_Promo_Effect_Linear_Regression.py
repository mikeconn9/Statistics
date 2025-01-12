import pandas as pd
import numpy as np
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Generate mock data
n = 100  # Number of observations

data = pd.DataFrame({
    "Sales": np.random.randint(500, 1000, size=n),               # Sales (dependent variable)
    "Promotion": np.random.choice([0, 1], size=n, p=[0.7, 0.3]), # Promotion (binary variable)
    "Price": np.random.uniform(10, 50, size=n),                  # Price (control variable)
    "Seasonality": np.random.choice(["Winter", "Spring", "Summer", "Fall"], size=n)  # Seasonality (categorical)
})

# Encode Seasonality as one-hot
data = pd.get_dummies(data, columns=["Seasonality"], drop_first=True)

# Display the first few rows of the dataset
print(data.head())

# Define target variable (y) and features (X)
y = data["Sales"]
X = data.drop(columns=["Sales"])

# Add a constant term for the intercept
X = sm.add_constant(X)  # Required for statsmodels regression

# Convert boolean columns to numeric
X = X.astype(float)

# Fit the linear regression model
model = sm.OLS(y, X).fit()

# Print the model summary
print(model.summary())

# Predict sales
predictions = model.predict(X)

# Plot actual vs. predicted
sns.scatterplot(x=y, y=predictions)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.show()

# Results:
'''
                            OLS Regression Results
==============================================================================
Dep. Variable:                  Sales   R-squared:                       0.012
Model:                            OLS   Adj. R-squared:                 -0.041
Method:                 Least Squares   F-statistic:                    0.2293
Date:                Wed, 25 Dec 2024   Prob (F-statistic):              0.949
Time:                        17:47:44   Log-Likelihood:                -638.44
No. Observations:                 100   AIC:                             1289.
Df Residuals:                      94   BIC:                             1305.
Df Model:                           5
Covariance Type:            nonrobust
======================================================================================
                         coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------
const                763.6337     58.132     13.136      0.000     648.212     879.056
Promotion            -29.8247     32.065     -0.930      0.355     -93.490      33.840
Price                  0.1717      1.337      0.128      0.898      -2.482       2.826
Seasonality_Spring    -0.9990     40.971     -0.024      0.981     -82.348      80.350
Seasonality_Summer    -9.8759     43.977     -0.225      0.823     -97.194      77.442
Seasonality_Winter   -22.1292     46.054     -0.481      0.632    -113.570      69.312
==============================================================================
Omnibus:                       44.758   Durbin-Watson:                   2.395
Prob(Omnibus):                  0.000   Jarque-Bera (JB):                6.695
Skew:                          -0.071   Prob(JB):                       0.0352
Kurtosis:                       1.740   Cond. No.                         172.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

'''