from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

def train_model(X, y):

    print("🚀 Training model...")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=150,
        max_depth=6,
        random_state=42
    )

    model.fit(X_train, y_train)

    joblib.dump(model, "models/model.pkl")

    print("✅ Model saved!")

    return model, X_test, y_test