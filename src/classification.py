from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = SVC(kernel='linear')
    model.fit(X_train, y_train)
    
    print(f"Model Accuracy: {model.score(X_test, y_test):.2f}")
    return model

if __name__ == "__main__":
    import numpy as np
    X = np.random.rand(100, 10)  # Simulated EEG features
    y = np.random.choice(['left', 'right', 'blink'], 100)
    
    model = train_model(X, y)
