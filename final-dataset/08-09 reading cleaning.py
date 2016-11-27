import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats
import statsmodels.formula.api as sm

df1 = pd.read_csv("Reading 08-09.csv")
df2 = pd.read_csv("Reading 09-10.csv")
df2.drop(df2.columns[[0,1,3]], inplace=True, axis=1)
df3 = pd.read_csv("Reading 10-11.csv")
df3.drop(df3.columns[[0,1,3]], inplace=True, axis=1)
df4 = pd.read_csv("Reading 11-12.csv")
df4.drop(df4.columns[[0,1,3]], inplace=True, axis=1)

merged = pd.merge(pd.merge(pd.merge
    (df1, df2, left_on="LEAID", right_on="LEAID"),
        df3, left_on="LEAID", right_on="LEAID"),
            df4, left_on="LEAID", right_on="LEAID")

wee = [1]
for x in range (4, 900, 2):
    wee.append(x)

merged.drop(merged.columns[wee], axis=1, inplace=True)
merged.rename(columns = {"STNAM": "STATE", "LEAID": "DISTRICT_ID", "leanm08": "DISTRICT/COUNTY"}, inplace=True)

merged.columns = merged.columns.str.replace('pctprof', '')
merged.columns = merged.columns.str.replace('RLA', 'READING_GRADE')
merged['STATE'] = merged['STATE'].str.lower()
merged['DISTRICT/COUNTY'] = merged['DISTRICT/COUNTY'].str.lower()
merged = merged.replace('^[A-Z]{2}', np.nan, regex=True)
merged = merged.replace('n/a', np.nan)

merged.to_csv("Reading08-11.csv")
