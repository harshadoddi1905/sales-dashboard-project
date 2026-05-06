import pandas as pd

# LOAD DATA
df = pd.read_csv("data/sales.csv", encoding='latin1')

# Preview data
print("\nPreview of Data:")
print(df.head())

# DATA CLEANING

# Convert date columns
df['Order_Date'] = pd.to_datetime(df['Order_Date'], dayfirst=True)
df['Ship_Date'] = pd.to_datetime(df['Ship_Date'], dayfirst=True)

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.fillna(0)

# Create Month-Year column
df['Month'] = df['Order_Date'].dt.to_period('M')

# DATA ANALYSIS

# Revenue by Region
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

# Top 5 Products
top_products = df.groupby('Product_Name')['Sales'].sum().sort_values(ascending=False).head(5)

# Monthly Sales Trend
monthly_sales = df.groupby('Month')['Sales'].sum()

# KPI CALCULATIONS

total_sales = df['Sales'].sum()
total_orders = df['Order_ID'].nunique()
avg_order_value = total_sales / total_orders

# CLEAN OUTPUT DISPLAY

print("\n" + "="*50)
print("SALES ANALYSIS SUMMARY")
print("="*50)

print(f"\nTotal Sales: ${total_sales:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Average Order Value: ${avg_order_value:,.2f}")

print("\n" + "-"*50)
print("Sales by Region")
print("-"*50)
print(region_sales.to_string())

print("\n" + "-"*50)
print("Top 5 Products")
print("-"*50)
print(top_products.to_string())

print("\n" + "-"*50)
print("Monthly Sales Trend")
print("-"*50)
print(monthly_sales.to_string())

print("\n" + "="*50)
print("Data cleaned and saved successfully!")
print("="*50)

# SAVE CLEANED DATA

df.to_csv("output/cleaned_sales.csv", index=False)

import matplotlib.pyplot as plt

# Create dashboard folder automatically
import os
os.makedirs("dashboard", exist_ok=True)

# 1. Monthly Sales Trend
monthly_sales.plot(figsize=(10,5))
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.savefig("dashboard/monthly_sales.png")
plt.show()

# 2. Sales by Region
region_sales.plot(kind='bar', figsize=(8,5))
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.savefig("dashboard/region_sales.png")
plt.show()

# 3. Top Products
top_products.plot(kind='bar', figsize=(8,5))
plt.title("Top 5 Products")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.savefig("dashboard/top_products.png")
plt.show()