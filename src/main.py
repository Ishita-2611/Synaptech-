from acquisition import acquire_eeg
from preprocessing import preprocess_eeg
from classification import train_model
from control import control_laptop
import numpy as np

# Load or train the model
X = np.random.rand(100, 10)  # Simulated EEG features
y = np.random.choice(['left', 'right', 'click'], 100)
model = train_model(X, y)

print("Starting Real-Time BCI Control...")

while True:
    raw_data = acquire_eeg()
    clean_data = preprocess_eeg(raw_data)
    features = clean_data.mean(axis=1).reshape(1, -1)  # Simple feature extraction
    action = model.predict(features)[0]
    
    print(f"Detected Action: {action}")
    control_laptop(action)
