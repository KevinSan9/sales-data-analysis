import os
import pandas as pd
import matplotlib.pyplot as plt

# Create output folder for graphics
os.makedirs("graphics", exist_ok=True)

# Load data
df = pd.read_csv("Data/Sample - Superstore.csv", encoding="latin1")

# Basic cleaning
df = df.drop_duplicates()
df = df.dropna()

# Clean column names just in case
df.columns = df.columns.str.strip()

# Convert date column
df["Order Date"] = pd.to_datetime(df["Order Date"])

# -----------------------------
# 1. Sales by Category
# -----------------------------
sales_category = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8, 5))
sales_category.plot(kind="bar")

plt.title("Sales by Category", fontsize=14)
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

plt.savefig("graphics/sales_by_category.png", dpi=200, bbox_inches="tight")
plt.close()
print("Saved graphic: graphics/sales_by_category.png")

# -----------------------------
# 2. Top 10 Products by Sales
# -----------------------------
top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values(ascending=True)
)

plt.figure(figsize=(12, 7))
top_products.plot(kind="barh")

plt.title("Top 10 Products by Sales", fontsize=14)
plt.xlabel("Total Sales")
plt.ylabel("Product")
plt.grid(axis="x", linestyle="--", alpha=0.7)
plt.tight_layout()

plt.savefig("graphics/top_products.png", dpi=200, bbox_inches="tight")
plt.close()
print("Saved graphic: graphics/top_products.png")

# -----------------------------
# 3. Monthly Sales Trend
# -----------------------------
monthly_sales = (
    df.set_index("Order Date")
    .resample("ME")["Sales"]
    .sum()
)

plt.figure(figsize=(12, 6))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend", fontsize=14)
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("graphics/monthly_sales.png", dpi=200, bbox_inches="tight")
plt.close()
print("Saved graphic: graphics/monthly_sales.png")

# -----------------------------
# 4. Simple insights
# -----------------------------
top_category = sales_category.idxmax()
top_region = df.groupby("Region")["Sales"].sum().idxmax()

print("Top category:", top_category)
print("Top region:", top_region)