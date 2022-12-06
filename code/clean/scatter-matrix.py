import pandas as pd
import numpy as np
from pandas.plotting import scatter_matrix

Path.cwd()

src_file = Path.home() / 'git' / 'python-data-visualization' / 'code' / 'data' / 'raw' / 'EPA_fuel_economy.csv'

df = pd.read_csv(src_file)

# Get 6 most common classes
counts = df['VClass'].value_counts()
car_class = counts.index.tolist()[0:6]
car_class

car_class_df = (df[['cylinders', 'fuelCost08', 'co2', 'VClass', 'displ']]
                .query('VClass in @car_class'))

car_class_df.head()

car_class_df.shape

scatter_matrix(car_class_df, figsize=(10,10), alpha = 0.5);