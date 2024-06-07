# Sales Data Analysis Project

This project contains scripts for analyzing and visualizing sales data from a sample CSV file. The analyses include identifying top-selling products, visualizing sales over time, and creating a choropleth map to display sales distribution by country.

## Project Structure

The project consists of three separate Python scripts:

1. `sale_sample_top_plot.py`: Generates a bar chart of the top-selling products.
2. `sale_sample_time_plot.py`: Creates a time series plot of monthly sales.
3. `sale_sample_geo_plot.py`: Produces a choropleth map showing the distribution of sales by country.
4. `sales_sample_data_analysis.py`: Produces all the plots with a single script

## Data

The analysis is based on a sample sales data CSV file (`sales_data_sample.csv`). The file should be located at `C:/Users/Pedro/Downloads/sales_data_sample.csv` in de scripts, but can be dowloaded at https://www.kaggle.com/datasets/kyanyoga/sample-sales-data.

## Visualization
### Geo Plot
![sales_geo_plot](https://github.com/PedroOrfao/Sales_sample_plots/assets/168864377/47222d43-8594-4b94-a24a-ba2b61bb9652)
### Conclusion
The geo plot reveals that our sales are predominantly concentrated in France and other French-speaking countries. Since the store is likely located in France, considering only the sales data, it is understandable that local sales are high. However, the store does not have a significant presence in many other countries, which suggests a potential marketing issue rather than a shipping problem, as we do have sales in distant locations such as Australia. Given these insights, the store should prioritize expanding its geographical presence, initially targeting broader European markets and subsequently other continents.

### Time Plot
![sales_time_plot](https://github.com/PedroOrfao/Sales_sample_plots/assets/168864377/5d294f45-37bc-4914-9cf1-371a270f0d0d)
### Conclusion
The time plot indicates that sales are closely linked to holidays, which is expected given that the store specializes in selling toys. Sales peak significantly at the end of the year, while a noticeable decline occurs around May. To address these seasonal fluctuations, the store should consider diversifying its product range to stabilize cash flow. Additionally, implementing targeted promotions and advertisements during low-sales months could help maintain a steady sales volume throughout the year.

### Top Products Plot
![sales_top_print](https://github.com/PedroOrfao/Sales_sample_plots/assets/168864377/ebabf1de-6e1d-4a5a-ba4c-9db9ca3bbbaa)
### Conclusion
The top products plot reveals that cars are the most sold toy by a significant margin, which is typical as most stores have a leading product. However, a concerning observation is the low sales of certain products, particularly trains. Train toys are globally recognized and enjoyed by both children and collectors, so they should not be the least sold item. To address this issue, the store should analyze its marketing strategies and pricing for train toys to understand why they are not performing as well as other products.

### License
This project is licensed under the MIT License. See the LICENSES file for details.

### Acknowledgements
Thanks to the folium project for providing the world-countries.json data used in the choropleth map example.
Thanks to Kyanyoga on Kaggle for providing the sample sales data used in this project.

## Installation

Ensure you have the required Python libraries installed. You can install the necessary libraries using pip:

```bash
pip install pandas matplotlib folium



