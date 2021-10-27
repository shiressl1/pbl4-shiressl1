# Problem 1
import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/nicholsons/comp0035_pbl4/master/data/paralympics_raw.csv?token'
    '=AHBUVRXMMNPI7VSWY4P34IDBO2TES')

pd.set_option('display.max_rows', df.shape[0] + 1)
pd.set_option('display.max_columns', df.shape[1] + 1)

print(df)