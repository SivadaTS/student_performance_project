import pandas as pd
import random

data = []

for i in range(100):
    hours_study = round(random.uniform(1, 10), 1)
    attendance = random.randint(50, 100)
    previous_score = random.randint(40, 90)
    sleep_hours = round(random.uniform(4, 9), 1)
    assignments_completed = random.randint(3, 10)
    internet_usage = round(random.uniform(1, 6), 1)

    # Formula to generate realistic final score
    final_score = (
        0.3 * hours_study * 10 +
        0.2 * attendance +
        0.3 * previous_score +
        0.1 * sleep_hours * 10 +
        0.1 * assignments_completed * 10 -
        0.1 * internet_usage * 5
    )

    final_score = round(min(max(final_score, 0), 100), 2)

    data.append([
        hours_study,
        attendance,
        previous_score,
        sleep_hours,
        assignments_completed,
        internet_usage,
        final_score
    ])

columns = [
    "hours_study",
    "attendance",
    "previous_score",
    "sleep_hours",
    "assignments_completed",
    "internet_usage",
    "final_score"
]

df = pd.DataFrame(data, columns=columns)
df.to_csv("student_data.csv", index=False)

print("✅ Dataset with 100 rows generated successfully!")