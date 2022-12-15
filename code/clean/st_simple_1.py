from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px 

@st.cache()
def load_data():
    src_file = Path.cwd().parent / 'data' / 'raw' / 'EPA_fuel_economy_summary.csv'
    df = pd.read_csv(src_file)
    return df

load_data().head()

# summarise the data by make
df = load_data()

df.head()

df.groupby('make').agg({'fuelCost08': ['mean', 'median', 'std']}).head()

fig = (px
    .histogram(
        load_data(),
        x = 'fuelCost08',
        color = 'class_summary',
        labels = {'fuelCost08': 'Annual Fuel Cost'},
        # template = 'seaborn',
        nbins = 40,
        title = 'Fuel Cost Distribution'
        ))

st.title('EPA Fuel Economy Data')
st.write(fig)

