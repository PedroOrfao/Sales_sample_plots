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

### Top Products Plot
![sales_top_print](https://github.com/PedroOrfao/Sales_sample_plots/assets/168864377/ebabf1de-6e1d-4a5a-ba4c-9db9ca3bbbaa)

## Installation

Ensure you have the required Python libraries installed. You can install the necessary libraries using pip:

```bash
pip install pandas matplotlib folium

