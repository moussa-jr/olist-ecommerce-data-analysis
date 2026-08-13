import pandas as pd
import matplotlib.pyplot as plt

# 1. Load dataset
df_sp = pd.read_csv('SP_Products_Analysis.csv')

# 2. Clean column names
df_sp.columns = df_sp.columns.str.strip()

# 3. Plotting Horizontal Bar Chart
plt.figure(figsize=(10, 6))
plt.barh(df_sp['product_category_name'], df_sp['category_sales'], color='salmon')

# 4. Customizing chart optics
plt.xlabel('Total Sales ($)', fontsize=12)
plt.title('Top 10 Product Categories in Sao Paulo', fontsize=14, fontweight='bold')
plt.gca().invert_yaxis()
plt.grid(axis='x', linestyle='--', alpha=0.7)

# 5. Format layout and show plot
plt.tight_layout()
plt.show()
