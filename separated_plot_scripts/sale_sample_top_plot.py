import pandas as pd
import matplotlib.pyplot as plt

url = 'C:/Users/Pedro/Downloads/sales_data_sample.csv'
df = pd.read_csv(url, encoding='ISO-8859-1')

product_sales = df.groupby('PRODUCTLINE')['QUANTITYORDERED'].sum().reset_index()
top_selling_products = product_sales.sort_values(by='QUANTITYORDERED', ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(top_selling_products['PRODUCTLINE'], top_selling_products['QUANTITYORDERED'], color='blue')
plt.title('Top Selling Products')
plt.xlabel('Product Line')
plt.ylabel('Quantity Ordered')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()

plt.show()
