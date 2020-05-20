import numpy as np
import pandas as pd
import itertools
from chord import Chord

data_url = 'dataTest.csv'
data = pd.read_csv(data_url)
data.head()

data.shape

# print(data)
pd.DataFrame(data.columns.values.tolist())

data = pd.DataFrame(data[['location', 'status']].values)
data

data = data.dropna()

data = data.replace('\n','', regex=True)
data

data = list(itertools.chain.from_iterable((i, i[::-1]) for i in data.values))
# print(data)
matrix = pd.pivot_table(
    pd.DataFrame(data), index=0, columns=1, aggfunc="size", fill_value=0
).values.tolist()

# print(data)

pd.DataFrame(matrix)

names = np.unique(data).tolist()
pd.DataFrame(names)

print(pd.DataFrame(names))

hex_colours = ["#3ADB79", "#DCEBE9", "#F5B32F", "#2AA9BB", "#EB1921", "#000000"]
# d3.schemeSet3
Chord(matrix, names, wrap_labels=True, colors=hex_colours).to_html()