import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import NearestNeighbors

# Mock Data: Callers who received follow-up service vs. didn't
data = pd.DataFrame({
    'age': [25, 30, 45, 35, 40, 50, 55, 60, 65, 70],
    'satisfaction_score': [7, 6, 8, 9, 7, 5, 8, 5, 4, 3],
    'received_followup': [1, 1, 1, 1, 0, 0, 1, 0, 0, 0]
})

# Calculate propensity scores
X = data[['age', 'satisfaction_score']]
y = data['received_followup']
logreg = LogisticRegression()
logreg.fit(X, y)
data['propensity_score'] = logreg.predict_proba(X)[:, 1]

# Perform matching
treated = data[data['received_followup'] == 1]
control = data[data['received_followup'] == 0]
nn = NearestNeighbors(n_neighbors=1).fit(control[['propensity_score']])
distances, indices = nn.kneighbors(treated[['propensity_score']])

# Matched control group
matched_control = control.iloc[indices.flatten()]
print("Matched Control Group:", matched_control)

#Matched Control Group:    age  satisfaction_score  received_followup  propensity_score
#4   40                   7                  0           0.73173
#4   40                   7                  0           0.73173
#4   40                   7                  0           0.73173
#4   40                   7                  0           0.73173
#4   40                   7                  0           0.73173