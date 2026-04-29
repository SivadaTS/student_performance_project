🎓 Student Performance Prediction
This project is a Machine Learning application built with Python that predicts a student's final academic score based on their daily habits and previous performance. It demonstrates a complete end-to-end ML workflow, from dataset creation to model deployment.

🚀 Overview
The goal of this project is to help educators and students understand how different factors—like study hours, sleep, and attendance—impact final results. By using a Linear Regression model, the system analyzes historical data to provide a numeric prediction for new inputs.

🛠️ Tech Stack
Language: Python 3.14

Libraries: * Pandas: For data loading and manipulation.

Scikit-Learn: For building and training the Linear Regression model.

Tools: VS Code, GitHub Desktop.

📊 Dataset Features
The model is trained on a CSV dataset (student_data.csv) containing the following features:

Hours Study: Total hours spent studying per day.

Attendance: Percentage of classes attended.

Previous Score: Results from the last examination.

Sleep Hours: Average hours of sleep per night.

Assignments: Number of assignments completed (out of 10).

Internet Usage: Hours spent on the internet daily.

💻 How to Run
Clone the repository:

Bash
git clone https://github.com/SivadaTS/student_performance_project.git
Install Dependencies:

Bash
pip install pandas scikit-learn
Run the Prediction Script:

Bash
python student_prediction.py
📈 Results
The system provides a real-time prediction output in the terminal, allowing for quick "what-if" analysis of student performance based on varying inputs.


