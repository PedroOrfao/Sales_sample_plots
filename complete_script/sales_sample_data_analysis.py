import pandas as pd
import matplotlib.pyplot as plt
import folium
import webbrowser

url = 'C:/Users/Pedro/Downloads/sales_data_sample.csv'
df = pd.read_csv(url, encoding='ISO-8859-1')

# Get boolean DataFrame indicating null locations
null_locations = df.isnull()

# Filter and print locations where null values occur
for col in null_locations.columns:
    null_rows = null_locations.index[null_locations[col]].tolist()

#Checking if there are any null values
#   for row in null_rows:
#       print(f"Null value at row {row}, column {col}")

#finding the top selling products
product_sales = df.groupby('PRODUCTLINE').agg({'QUANTITYORDERED': 'sum'}).reset_index()
top_selling_products = product_sales.sort_values(by='QUANTITYORDERED', ascending=False)

#undesrtanding the sales with a time parameter
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'].str.strip(), errors='coerce')

# Ensure no invalid dates
df = df.dropna(subset=['ORDERDATE'])

# Set 'ORDERDATE' as the index
df.set_index('ORDERDATE', inplace=True)

# Resample the data to get monthly totals
monthly_sales = df['QUANTITYORDERED'].resample('M').sum()

#understanding the sales with a global parameter
country_counts = df['COUNTRY'].value_counts(normalize=True).reset_index()
country_counts.columns = ['COUNTRY', 'COUNT']

#geoJSON with the country boundaries
#extracted from the repository: python-visualization/folium
geo_json_data = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json'

#folium map
map = folium.Map(location=[20,0], zoom_start =2)
folium.Choropleth(
    geo_data=geo_json_data,
    name='Choropleth map',
    data=country_counts,
    columns=['COUNTRY','COUNT'],
    key_on='feature.properties.name',
    fill_color='YlOrRd',
    fill_opacity=0.6,
    line_opacity=0.2,
    legend_name='Country Counts'
).add_to(map)

map.save('choropleth_sale_map.html')

#Top selling products plot
#plt.figure(figsize=(12,6))
plt.bar(top_selling_products['PRODUCTLINE'], top_selling_products['QUANTITYORDERED'], color='blue')
plt.title('Top Selling Products')
plt.xlabel('Product Line')
plt.ylabel('Quantity Ordered')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()

#time plot
plt.figure(figsize=(12,6))
plt.plot(monthly_sales.index, monthly_sales, label='Quantity', color='green')
plt.title('Time Series Plot')
plt.xlabel('date')
plt.ylabel('Quantity')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

#displaying everything
plt.show()

webbrowser.open('choropleth_sale_map.html')
