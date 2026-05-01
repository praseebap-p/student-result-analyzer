data["Status"] = data["Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")

print("\nSummary:")
print(data.describe())

data.to_csv("report.csv", index=False)
