import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("UberDataset.csv")

print(df.head())
print(df.info())
print(df.describe())

df.dropna(subset=["START_DATE","END_DATE","CATEGORY","START","STOP"], inplace=True)
df["PURPOSE"] = df["PURPOSE"].fillna("Unknown")
df["START_DATE"] = pd.to_datetime(
    df["START_DATE"],
    format="mixed",
    errors="coerce"
)

df["END_DATE"] = pd.to_datetime(
    df["END_DATE"],
    format="mixed",
    errors="coerce"
)

# Remove rows with invalid dates
df.dropna(subset=["START_DATE", "END_DATE"], inplace=True)

df["Hour"] = df["START_DATE"].dt.hour
df["Day"] = df["START_DATE"].dt.day
df["Month"] = df["START_DATE"].dt.month
df["Weekday"] = df["START_DATE"].dt.day_name()
df["Duration"] = (df["END_DATE"]-df["START_DATE"]).dt.total_seconds()/60

plt.figure(figsize=(6,5))
sns.countplot(x="CATEGORY", data=df)
plt.title("Ride Category Distribution")
plt.show()

plt.figure(figsize=(10,5))
sns.countplot(x="Hour", data=df)
plt.title("Ride Distribution by Hour")
plt.show()

weekday_order=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
plt.figure(figsize=(10,5))
sns.countplot(x="Weekday", data=df, order=weekday_order)
plt.xticks(rotation=30)
plt.title("Ride Distribution by Weekday")
plt.show()

plt.figure(figsize=(8,5))
sns.countplot(x="Month", data=df)
plt.title("Monthly Ride Trend")
plt.show()

top_start=df["START"].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_start.values,y=top_start.index)
plt.title("Top 10 Pickup Locations")
plt.show()

top_stop=df["STOP"].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_stop.values,y=top_stop.index)
plt.title("Top 10 Drop Locations")
plt.show()

plt.figure(figsize=(10,6))
sns.countplot(y="PURPOSE", data=df, order=df["PURPOSE"].value_counts().index)
plt.title("Trip Purpose Distribution")
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(df["MILES"], bins=30, kde=True)
plt.title("Trip Distance Distribution")
plt.show()

plt.figure(figsize=(6,5))
sns.barplot(x="CATEGORY", y="MILES", data=df)
plt.title("Average Trip Distance by Category")
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(df["Duration"], bins=30, kde=True)
plt.title("Trip Duration Distribution")
plt.show()

numeric_df=df.select_dtypes(include=np.number)
plt.figure(figsize=(8,6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="Blues")
plt.title("Correlation Heatmap")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x=df["MILES"])
plt.title("Outlier Detection for Trip Distance")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x="CATEGORY", y="MILES", data=df)
plt.title("Trip Distance by Category")
plt.show()

print("Analysis completed successfully.")
