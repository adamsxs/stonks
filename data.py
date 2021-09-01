import numpy as np
import pandas as pd
import plotly_express as px

print('hi')

#if "__name__" == "__main__":

gme_df = pd.read_csv("C:\\Users\\michaelmayer\\Downloads\\GME2themoon.csv")
#print(gme_df.info())
#print(gme_df.head())
print(gme_df.shape)

gme_df['dt'] = pd.to_datetime(gme_df['Dates'])
print(gme_df.head())

#gme_df.rolling('15m')
#window, min_periods=None, center=False, win_type=None, on=None, axis=0, closed=None, method='single')
print(gme_df.groupby(pd.Grouper(key='dt',freq='15min')))

size_per_fifteen_mins = gme_df.groupby(pd.Grouper(key='dt',freq='15min'))[['Size']].sum()
print(size_per_fifteen_mins)