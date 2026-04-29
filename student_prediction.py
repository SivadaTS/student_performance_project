# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load dataset
data = pd.read_csv("student_data.csv")

# Features (inputs)
X = data[['hours_study', 'attendance', 'previous_score',
          'sleep_hours', 'assignments_completed', 'internet_usage']]

# Target (output)
y = data['final_score']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
error = mean_absolute_error(y_test, predictions)

print("\n📊 Model Evaluation")
print("----------------------")
print(f"Mean Absolute Error: {error:.2f}")

print("\n📌 Sample Predictions")
print("----------------------")
for i in range(len(predictions)):
    print(f"Predicted: {predictions[i]:.2f}, Actual: {y_test.iloc[i]}")

# ================= USER INPUT =================

print("\n🎓 Student Performance Prediction")
print("----------------------------------")

try:
    hours = float(input("Enter study hours (1–10): "))
    attendance = float(input("Enter attendance (%): "))
    previous = float(input("Enter previous score: "))
    sleep = float(input("Enter sleep hours: "))
    assignments = int(input("Assignments completed (out of 10): "))
    internet = float(input("Internet usage (hours/day): "))

    new_data = [[hours, attendance, previous, sleep, assignments, internet]]

    result = model.predict(new_data)

    print(f"\n🎯 Predicted Final Score: {result[0]:.2f}")

except ValueError:
    print("❌ Invalid input! Please enter correct numeric values.")