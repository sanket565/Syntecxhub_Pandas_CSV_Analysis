import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load dataset
df = pd.read_csv("datasets/students.csv")

print("Dataset Loaded Successfully\n")

# Display first rows
print("First 5 Rows:")
print(df.head())

# Dataset info
print("\nDataset Information:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Mean marks
print("\nAverage Marks:", df["Marks"].mean())

# Filter top students
top_students = df[df["Marks"] > 85]

print("\nTop Performing Students:")
print(top_students)

# Save filtered data
top_students.to_csv("outputs/top_students.csv", index=False)

# Average marks by city
city_avg = df.groupby("City")["Marks"].mean()

print("\nAverage Marks by City:")
print(city_avg)

# Visualization 1: Marks Distribution
plt.figure()
sns.histplot(df["Marks"])
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.savefig("charts/marks_distribution.png")

# Visualization 2: Average Marks by City
plt.figure()
city_avg.plot(kind="bar")
plt.title("Average Marks by City")
plt.xlabel("City")
plt.ylabel("Average Marks")
plt.savefig("charts/city_average_marks.png")

print("\nAnalysis Completed Successfully!")



with open("outputs/analysis_report.txt", "w") as f:
    f.write("Data Analysis Report\n")
    f.write("--------------------\n")
    f.write(f"Average Marks: {df['Marks'].mean()}\n")
    f.write(f"Maximum Marks: {df['Marks'].max()}\n")
    f.write(f"Minimum Marks: {df['Marks'].min()}\n")