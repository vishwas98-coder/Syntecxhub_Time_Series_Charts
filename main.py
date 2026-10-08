import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual theme
sns.set_theme(style="whitegrid")

# Load and preprocess dataset
df = pd.read_csv("sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

# ---------------------------------------------------------
# 1. Line Chart: Sales Over Time (Monthly Aggregation)
# ---------------------------------------------------------
monthly_sales = df.resample("ME", on="Date")["Sales"].sum().reset_index()
monthly_sales["Month"] = monthly_sales["Date"].dt.strftime("%b %Y")

plt.figure(figsize=(10, 5))
plt.plot(monthly_sales["Month"], monthly_sales["Sales"], marker="o", color="#1f77b4", linewidth=2)
plt.title("Total Sales Trend over Time (Monthly Aggregation)", fontsize=14)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Total Sales ($)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# 2. Bar Chart: Category Comparison
# ---------------------------------------------------------
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(x=category_sales.index, y=category_sales.values, palette="Blues_r")
plt.title("Total Sales by Category", fontsize=14)
plt.xlabel("Category", fontsize=12)
plt.ylabel("Total Sales ($)", fontsize=12)
plt.tight_layout()
plt.savefig("category_sales_bar.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# 3. Pie Chart: Category Share
# ---------------------------------------------------------
plt.figure(figsize=(7, 7))
plt.pie(category_sales, labels=category_sales.index, autopct="%1.1f%%", startangle=140, colors=sns.color_palette("pastel"))
plt.title("Sales Percentage Share by Category", fontsize=14)
plt.tight_layout()
plt.savefig("category_share_pie.png", dpi=300)
plt.close()

print("All charts generated and saved as PNG files!")
