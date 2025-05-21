# backend/train_model.py

from sklearn.linear_model import LinearRegression
from joblib import dump

# Dummy training data
X_train = [
    [12.9, 80.1, 10.0, 45],
    [13.0, 80.2, 12.5, 90],
    [13.1, 80.3, 8.0, 120],
    [13.2, 80.4, 15.0, 270],
]

y_train = [0.8, 0.4, 0.9, 0.2]  # threat risk scores

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
dump(model, "model.pkl")
print("✅ model.pkl saved in backend/")
