import pandas as pd


data_source = pd.read_html('https://pythonprogramming.net/parsememcparseface/')


for ds in data_source:
    print(ds)
