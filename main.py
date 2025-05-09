import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from credenciales import API_KEY

from fredapi import Fred

plt.style.use('fivethirtyeight')
pd.set_option('display.max_columns', 500)
color_pal = plt.rcParams['axes.prop_cycle'].by_key()['color']

#1. Create The Fred Object
fred = Fred(api_key=API_KEY)

#2. Search for economic data!
sp_search = fred.search('S&P', order_by='popularity')
#print(sp_search.head())

#3. Pull Raw Data
sp500 = fred.get_series(series_id='SP500')
sp500.plot()