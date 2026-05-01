import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("students.csv")

print("Average Marks:", data["Marks"].mean())
print("Topper:", data.loc[data["Marks"].idxmax()])

data.plot(x="Name", y="Marks", kind="bar")
plt.show()
