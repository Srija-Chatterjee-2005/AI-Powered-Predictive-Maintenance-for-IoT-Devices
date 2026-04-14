import sys
import os

sys.path.append(os.path.abspath("src"))

from data_preprocessing import load_data, preprocess
from model_training import train_model
from visualization import generate_all_plots
from sklearn.metrics import accuracy_score

# Load data
df = load_data("data/sensor_data.csv")

# Preprocess
X, y, df_clean = preprocess(df)

# Train model
model, X_test, y_test = train_model(X, y)

# Predict
y_pred = model.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, y_pred)
#print(f"Model Accuracy: {acc*100:.2f}%")#

print("✅ Model Training Completed")
print(f"📊 Model Accuracy: {acc*100:.2f}%")

# Generate plots
generate_all_plots(df_clean, y_test, y_pred, model)

print("🎉 All outputs generated successfully!")