import pandas as pd
import folium
import webbrowser

url = 'C:/Users/Pedro/Downloads/sales_data_sample.csv'
df = pd.read_csv(url, encoding='ISO-8859-1')

columns_to_clean = ['ADDRESSLINE2', 'STATE', 'TERRITORY']
df[columns_to_clean] = df[columns_to_clean].fillna('missing')

country_counts = df['COUNTRY'].value_counts(normalize=True).reset_index()
country_counts.columns = ['COUNTRY', 'COUNT']

geo_json_data = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json'

# Folium map
map = folium.Map(location=[20, 0], zoom_start=2)
folium.Choropleth(
    geo_data=geo_json_data,
    name='Choropleth map',
    data=country_counts,
    columns=['COUNTRY', 'COUNT'],
    key_on='feature.properties.name',
    fill_color='YlOrRd',
    fill_opacity=0.6,
    line_opacity=0.2,
    legend_name='Country Counts'
).add_to(map)

map.save('choropleth_sales_map.html')

webbrowser.open('choropleth_sales_map.html')
