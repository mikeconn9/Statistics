import statsmodels.api as sm
import pandas as pd

# Mock Data: Pre/Post intervention satisfaction scores for treated and control groups
data = pd.DataFrame({
    'group': ['treated', 'treated', 'treated', 'treated', 'treated', 'control', 'control', 'control', 'control', 'control'],
    'time': ['pre', 'pre', 'post', 'post', 'pre', 'post', 'pre', 'pre', 'post', 'post'],
    'satisfaction': [6, 8, 9, 5, 5, 6, 7, 9, 9, 4]
})

# Encode categorical variables
data['group_encoded'] = (data['group'] == 'treated').astype(int)
data['time_encoded'] = (data['time'] == 'post').astype(int)
data['interaction'] = data['group_encoded'] * data['time_encoded']

# Run Difference-in-Differences regression
X = data[['group_encoded', 'time_encoded', 'interaction']]
y = data['satisfaction']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())

#UserWarning: kurtosistest only valid for n>=20 ... continuing anyway, n=10
#  k, _ = kurtosistest(a, axis)
#                            OLS Regression Results
#==============================================================================
#Dep. Variable:           satisfaction   R-squared:                       0.135
#Model:                            OLS   Adj. R-squared:                 -0.297
#Method:                 Least Squares   F-statistic:                    0.3122
#Date:                Mon, 27 Jan 2025   Prob (F-statistic):              0.816
#Time:                        14:48:17   Log-Likelihood:                -19.217
#No. Observations:                  10   AIC:                             46.43
#Df Residuals:                       6   BIC:                             47.64
#Df Model:                           3
#Covariance Type:            nonrobust
#=================================================================================
#                    coef    std err          t      P>|t|      [0.025      0.975]
#---------------------------------------------------------------------------------
#const             8.0000      1.509      5.301      0.002       4.307      11.693
#group_encoded    -1.6667      1.948     -0.855      0.425      -6.434       3.101
#time_encoded     -1.6667      1.948     -0.855      0.425      -6.434       3.101
#interaction       2.3333      2.755      0.847      0.430      -4.409       9.076
#==============================================================================
#Omnibus:                        1.601   Durbin-Watson:                   1.967
#Prob(Omnibus):                  0.449   Jarque-Bera (JB):                0.790
#Skew:                           0.187   Prob(JB):                        0.674
#Kurtosis:                       1.675   Cond. No.                         7.01
#==============================================================================
#
#Notes:
#[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
