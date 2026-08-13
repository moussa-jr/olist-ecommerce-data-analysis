import pandas as pd
import matplotlib.pyplot as plt

# 1. Load dataset
df_cities = pd.read_csv('Olist_Top_Cities_Performance.csv')

# 2. Clean column names and data
df_cities.columns = df_cities.columns.str.strip()
df_cities = df_cities.dropna(subset=['customer_city'])
df_cities['customer_city'] = df_cities['customer_city'].astype(str)

# 3. Plotting Top Cities
plt.figure(figsize=(12, 7))
plt.bar(df_cities['customer_city'], df_cities['total_sales'], color='teal', edgecolor='black')

# 4. Customizing chart optics
plt.title('Top 10 Cities by Total Sales (Olist)', fontsize=16, fontweight='bold')
plt.xlabel('City Name', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)

# 5. Display plot
plt.show()
