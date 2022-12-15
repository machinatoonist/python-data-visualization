from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px 
import altair as alt

@st.cache()
def load_data():
    src_file = Path.cwd().parent / 'data' / 'raw' / 'EPA_fuel_economy_summary.csv'
    raw_df = pd.read_csv(src_file)
    return raw_df

# Load data and determine valid values
df = load_data()
min_year = int(df['year'].min())
max_year = int(df['year'].max())

# Add ALL as an option to make it easier to select all makes
valid_makes = ['ALL'] + sorted(df['make'].unique())

# Get the top 5 makes as the default
default_makes = df['make'].value_counts().nlargest(5).index.tolist()

# Setup the UI with a multi-select for the makes
st.title('EPA Fuel Economy Data - sidebar example')
make = st.sidebar.multiselect("Select a make:", valid_makes, default=default_makes)
year_range = st.sidebar.slider(
    label = 'Year Range', 
    min_value = min_year, 
    max_value = max_year, 
    value = (min_year, max_year))

# Filter data based on inputs
year_filter = df['year'].between(year_range[0], year_range[1])
if 'ALL' in make:
    # Dummy filter to select all makes
    make_filter = True
else:
    make_filter = df['make'].isin(make)

# Create dataframe for plotting
plot_df = df[year_filter & make_filter]

avg_fuel_economy = plot_df['fuelCost08'].mean().round(0)
st.sidebar.metric('Average Fuel Economy', f'${avg_fuel_economy:,.0f}')
avg_mpg = plot_df['comb08'].mean().round(0)
st.sidebar. metric('Average mileage', f'{avg_mpg:,.0f} mpg')

# Plot the data
fig = (px
    .histogram(
        plot_df,
        x = 'fuelCost08',
        color = 'class_summary',
        labels = {'fuelCost08': 'Annual Fuel Cost'},
        nbins = 40,
        title = 'Fuel Cost Distribution'
        ))

altair_chart = (alt.Chart(plot_df)
    .mark_tick()
    .encode(y = 'fuel_type_summary', x = 'barrels08')
    )

# Display the output results
st.write(fig)
st.write(altair_chart)
st.write("Sample data", plot_df.head(10))
