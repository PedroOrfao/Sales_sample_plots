import pandas as pd
import matplotlib.pyplot as plt

url = 'C:/Users/Pedro/Downloads/sales_data_sample.csv'
df = pd.read_csv(url, encoding='ISO-8859-1')

df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'].str.strip(), errors='coerce')

df = df.dropna(subset=['ORDERDATE'])

df.set_index('ORDERDATE', inplace=True)

monthly_sales = df['QUANTITYORDERED'].resample('M').sum()

plt.figure(figsize=(12, 6))
plt.plot(monthly_sales.index, monthly_sales, label='Quantity', color='green')
plt.title('Monthly Sales')
plt.xlabel('Date')
plt.ylabel('Quantity')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
