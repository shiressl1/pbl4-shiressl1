# Problem 2
import pandas as pd

df = pd.read_csv('data/paralympics_raw.csv')

pd.set_option('display.max_rows', df.shape[0] + 1)
pd.set_option('display.max_columns', df.shape[1] + 1)

# Print the number of rows and columns in the DataFrame
print(df.shape)

# Print the first 5 rows of data
print(df.head(5))

# Print the column labels
# print(df.columns)

# Print the column labels and data types
print(df.info(verbose=True))
