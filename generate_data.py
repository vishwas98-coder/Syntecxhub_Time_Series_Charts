import pandas as pd
import numpy as np

# Set random seed for consistent results
np.random.seed(42)

# Generate 500 sales records across 2024
dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq="D")
categories = ["Electronics", "Clothing", "Home & Kitchen", "Books"]

data = {
    "Date": np.random.choice(dates, size=500),
    "Category": np.random.choice(categories, size=500, p=[0.4, 0.3, 0.2, 0.1]),
    "Sales": np.random.randint(20, 500, size=500)
}

df = pd.DataFrame(data)
df.to_csv("sales_data.csv", index=False)
print("sales_data.csv generated successfully!")
