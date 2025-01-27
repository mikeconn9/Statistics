from sklearn.svm import OneClassSVM
import numpy as np
import pandas as pd

# Mock Data: Call center data with customer satisfaction scores
np.random.seed(42)
# Normal data
normal_data = np.random.normal(loc=7, scale=1.5, size=100).reshape(-1, 1)
# Anomalous data
anomalous_data = np.random.uniform(low=0, high=2, size=5).reshape(-1, 1)
data = np.vstack((normal_data, anomalous_data))
labels = np.array([0] * 100 + [1] * 5)  # 0 = normal, 1 = anomaly

# Fit One-Class SVM
one_class_svm = OneClassSVM(kernel="rbf", gamma=0.1, nu=0.05)  # nu is the anomaly ratio
predictions = one_class_svm.fit_predict(data)

# Map predictions: -1 = anomaly, 1 = normal
predictions = np.where(predictions == -1, 1, 0)

# Compare actual labels with predictions
df = pd.DataFrame({'Satisfaction_Score': data.flatten(), 'Actual': labels, 'Predicted': predictions})
print(df)

#     Satisfaction_Score  Actual  Predicted
#0              7.745071       0          0
#1              6.792604       0          0
#2              7.971533       0          0
#3              9.284545       0          0
#4              6.648770       0          0
#..                  ...     ...        ...
#100            0.834822       1          0
#101            0.444216       1          1
#102            0.239731       1          1
#103            0.675230       1          0
#104            1.885819       1          0
#
#[105 rows x 3 columns]