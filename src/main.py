import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

def load_data(filepath):
    # Placeholder: Load your dataset here
    # df = pd.read_csv(filepath)
    # For now, using sample data
    data = {
        'hours_studied': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'attendance': [80, 85, 90, 95, 100, 85, 90, 95, 100, 95],
        'performance': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
    }
    df = pd.DataFrame(data)
    return df

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Mean Squared Error: {mse}")
    return model

def save_model(model, filepath):
    joblib.dump(model, filepath)

def main():
    df = load_data('data/student_data.csv')  # Placeholder path
    X = df[['hours_studied', 'attendance']]
    y = df['performance']
    model = train_model(X, y)
    save_model(model, 'models/performance_model.pkl')
    print("Model trained and saved.")

if __name__ == "__main__":
    main()