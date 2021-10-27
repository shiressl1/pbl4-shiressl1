# Problem 3: Delete any unnecessary columns
import pandas as pd

df = pd.read_csv('data/paralympics_raw.csv')

pd.set_option('display.max_rows', df.shape[0] + 1)
pd.set_option('display.max_columns', df.shape[1] + 1)

print(df.info())
df.drop(['Events', 'Sports', 'Countries'], axis=1, inplace=True)
print(df.info())
