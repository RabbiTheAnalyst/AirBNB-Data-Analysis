# airbnb_analysis.py

# ====== IMPORTS ======
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ====== LOAD DATA ======
df = pd.read_csv("datasets.csv")  # Make sure the file is in same folder

# ====== CLEANING ======
# Drop rows with missing important data
df.dropna(subset=["neighbourhood", "latitude", "longitude", "price", "room_type"], inplace=True)

# Convert date column
df["last_review"] = pd.to_datetime(df["last_review"], errors='coerce')

# ====== BASIC INFO ======
print("Dataset shape:", df.shape)
print("Column names:", df.columns)
print("\nMissing values:\n", df.isnull().sum())




# ====== NEIGHBOURHOOD GROUP ======
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='neighbourhood_group', order=df['neighbourhood_group'].value_counts().index)
plt.title("Listings per Neighbourhood Group")
plt.xlabel("Neighbourhood Group")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("neighbourhood_group_count.png")
plt.close()

# ====== ROOM TYPE ======
plt.figure(figsize=(7, 4))
sns.countplot(data=df, x='room_type', order=df['room_type'].value_counts().index)
plt.title("Distribution of Room Types")
plt.xlabel("Room Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("room_type_distribution.png")
plt.close()

# ====== PRICE DISTRIBUTION ======
plt.figure(figsize=(8, 5))
sns.histplot(df[df["price"] < 500]["price"], bins=50, kde=True)
plt.title("Price Distribution (Price < $500)")
plt.xlabel("Price ($)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("price_distribution.png")
plt.close()

# ====== TOP NEIGHBOURHOODS ======
top_neigh = df["neighbourhood"].value_counts().head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_neigh.values, y=top_neigh.index, palette="viridis")
plt.title("Top 10 Neighbourhoods by Listings")
plt.xlabel("Number of Listings")
plt.ylabel("Neighbourhood")
plt.tight_layout()
plt.savefig("top_neighbourhoods.png")
plt.close()

# ====== AVAILABILITY vs REVIEWS ======
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="availability_365", y="number_of_reviews", alpha=0.4)
plt.title("Availability vs Number of Reviews")
plt.xlabel("Availability (days/year)")
plt.ylabel("Number of Reviews")
plt.tight_layout()
plt.savefig("availability_vs_reviews.png")
plt.close()

print("✅ Analysis completed. All plots saved successfully.")
# Additional code for descriptive statistics and groupby analysis

# Group by neighbourhood_group and calculate average price
avg_price_by_group = df.groupby('neighbourhood_group')['price'].mean().sort_values(ascending=False)

# Group by room_type and calculate average price and availability
room_type_stats = df.groupby('room_type')[['price', 'availability_365']].mean()

# Descriptive statistics of numeric columns
descriptive_stats = df.describe()

avg_price_by_group, room_type_stats, descriptive_stats
