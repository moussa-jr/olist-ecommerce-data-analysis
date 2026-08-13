import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv('Monthly_Sales_Summary.csv')

# 2. Create Year-Month period column
df['period'] = df['order_year'].astype(str) + '-' + df['order_month'].astype(str)

# 3. Plotting the trend
plt.figure(figsize=(12, 6))
plt.plot(df['period'], df['total_sales'], marker='o', color='b', linestyle='-', linewidth=2)

# 4. Customizing chart optics
plt.title('Monthly Total Sales Trend (Olist E-commerce)', fontsize=14)
plt.xlabel('Year-Month', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)

# 5. Display the plot
plt.show()
