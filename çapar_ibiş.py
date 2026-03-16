
import numpy as np
import IPython.display as display
from matplotlib import pyplot as plt
import io
import base64

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

fig = plt.figure(figsize=(4, 3), facecolor='w')
plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)
plt.title("Sample Visualization", fontsize=10)

data = io.BytesIO()
plt.savefig(data)
image = F"data:image/png;base64,{base64.b64encode(data.getvalue()).decode()}"
alt = "Sample Visualization"
display.display(display.Markdown(F"""![{alt}]({image})"""))
plt.close(fig)



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams["figure.figsize"] = (8,5)
sns.set_style("whitegrid")
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("dataset.xlsx")
df.head()
print("Dataset shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

# Convert 'EnergyConsumption' to numeric, coercing errors, then drop NaNs
df["EnergyConsumption"] = pd.to_numeric(df["EnergyConsumption"], errors='coerce')
df.dropna(subset=["EnergyConsumption"], inplace=True)

df.isnull().sum()
df.describe()
plt.hist(df["EnergyConsumption"], bins=20, edgecolor="black")
plt.title("Distribution of Energy Consumption")
plt.xlabel("Energy Consumption")
plt.ylabel("Frequency")
plt.show()
plt.scatter(df["Temperature"], df["EnergyConsumption"])
plt.title("Temperature vs Energy Consumption")
plt.xlabel("Temperature")
plt.ylabel("Energy Consumption")
plt.show()
plt.scatter(df["Occupancy"], df["EnergyConsumption"])
plt.title("Occupancy vs Energy Consumption")
plt.xlabel("Occupancy")
plt.ylabel("Energy Consumption")
plt.show()
avg_energy = df.groupby("DayOfWeek")["EnergyConsumption"].mean()

avg_energy.plot(kind="bar")
plt.title("Average Energy Consumption by Day of Week")
plt.xlabel("Day of Week")
plt.ylabel("Average Energy Consumption")
plt.show()
avg_energy = df.groupby("DayOfWeek")["EnergyConsumption"].mean()

avg_energy.plot(kind="bar")
plt.title("Average Energy Consumption by Day of Week")
plt.xlabel("Day of Week")
plt.ylabel("Average Energy Consumption")
plt.show()
numerical_cols = ["Temperature","Humidity","SquareFootage","Occupancy","RenewableEnergy","EnergyConsumption"]

corr = df[numerical_cols].corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
sns.boxplot(x=df["EnergyConsumption"])
plt.title("Boxplot of Energy Consumption")
plt.show()
plt.figure(figsize=(8,5))

sns.boxplot(x="DayOfWeek", y="EnergyConsumption", data=df)

plt.title("Energy Consumption Distribution by Day of Week")
plt.xlabel("Day of Week")
plt.ylabel("Energy Consumption")

plt.show()
sns.pairplot(df[["Temperature","Humidity","Occupancy","RenewableEnergy","EnergyConsumption"]])
plt.show()
