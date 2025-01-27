from sklearn.ensemble import IsolationForest
import numpy as np
import pandas as pd

# Mock Data: Call center data with call durations (normal and anomalous)
np.random.seed(42)
# Normal data
normal_data = np.random.normal(loc=10, scale=2, size=100).reshape(-1, 1)
# Anomalous data
anomalous_data = np.random.uniform(low=20, high=30, size=5).reshape(-1, 1)
data = np.vstack((normal_data, anomalous_data))
labels = np.array([0] * 100 + [1] * 5)  # 0 = normal, 1 = anomaly

# Fit Isolation Forest
iso_forest = IsolationForest(contamination=0.05, random_state=42)
predictions = iso_forest.fit_predict(data)

# Map predictions: -1 = anomaly, 1 = normal
predictions = np.where(predictions == -1, 1, 0)

# Compare actual labels with predictions
df = pd.DataFrame({'Call_Duration': data.flatten(), 'Actual': labels, 'Predicted': predictions})
print(df)

#     Call_Duration  Actual  Predicted
#0        10.993428       0          0
#1         9.723471       0          0
#0        10.993428       0          0
#1         9.723471       0          0
#1         9.723471       0          0
#2        11.295377       0          0
#3        13.046060       0          0
#2        11.295377       0          0
#3        13.046060       0          0
#3        13.046060       0          0
#4         9.531693       0          0
#..             ...     ...        ...
#100      24.174110       1          1
#101      22.221078       1          1
#102      21.198654       1          1
#103      23.376152       1          1
#104      29.429097       1          1