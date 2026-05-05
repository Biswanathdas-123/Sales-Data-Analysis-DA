import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('sales_data.csv')

# Display first rows
print(df.head())

# Total sales
total_sales = df['Sales'].sum()
print("Total Sales:", total_sales)

# Sales by category
category_sales = df.groupby('Category')['Sales'].sum()
print(category_sales)

# Plot sales chart
category_sales.plot(kind='bar')

plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales')

plt.show()
