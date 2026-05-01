import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("students.csv")

# Basic analysis
print("Average Marks:", data["Marks"].mean())
print("Topper:")
print(data.loc[data["Marks"].idxmax()])

print("\nPass/Fail Status:")
data["Status"] = data["Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")
print(data)

# Visualization
plt.figure(figsize=(8,5))
plt.bar(data["Name"], data["Marks"])
plt.title("Student Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
