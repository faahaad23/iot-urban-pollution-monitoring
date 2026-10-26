import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Step 1: Load your CSV data
df = pd.read_csv("iot_pollution_12hr.csv")  # your real data file

# Step 2: Select input (X) and target (y)
X = df[['Noise_dB', 'CO2_ppm']]
y = df['Temperature_C']

# Step 3: Train model
model = LinearRegression()
model.fit(X, y)

# Step 4: Save model using pickle
with open("pollution_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved successfully!")
